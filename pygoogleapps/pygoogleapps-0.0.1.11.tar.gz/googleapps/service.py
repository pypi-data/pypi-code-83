# Copyright (c) 2019-2021 Kevin Crouse
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @license: http://www.apache.org/licenses/LICENSE-2.0
# @author: Kevin Crouse (krcrouse@gmail.com)

import os, os.path
import datetime
import re
import shutil

import warnings
from pprint import pprint

import pickle
import google.auth, google.oauth2
import google_auth_oauthlib
import googleapiclient.discovery # to install this : pip install --upgrade google-api-python-client

#-------------- Notes on Permission Scope
# Permission Scopes are the Google-designed access scopes for all of the
# services provided. The generic GoogleApps.Service interface allows for all scopes,
# but the valuable elements of the suite will be missing. This allows you to create
# your own supported interfaces even if you don't intend to share.  But please share
# if it's any good.

# At present, the full list of Google Permission Scopes are listed here:
# https://developers.google.com/identity/protocols/googlescopes

# As specific interfaces are designed and added to this suite of Python GoogleApps package,
# they should be added to the directory below for auto-resolution

# We process scopes based on single intuitive keywords, but Google has a number of identifiers.
# This is the location where we map them. Users can also specify these independently

#  1. the Google API Name, which is a shorthand, clear descriptor
#  2. The API version
#  3. The Scope

DEFAULT_SCOPES = {
    'gmail': ['gmail', 'v1', 'gmail.send'],
    'sheets': ['sheets', 'v4', 'spreadsheets'],
    'sheets.readonly': ['sheets', 'v4', 'spreadsheets.readonly'],
    'drive': ['drive', 'v3', 'drive'],
    'drive.metadata': ['drive', 'v3', 'drive.metadata'],
    'drive.readonly': ['drive', 'v3', 'drive.readonly'],
    'docs': ['docs', 'v1', 'documents'],
}

class ServiceManager(object):
    '''
    The ServiceManager is intended to encapsulate all of the Google services for a user. The SM object must be tied to the registered OAUTH secret file, which the user must download from the Google Developer Console (https://console.developers.google.com/apis/credentials). The filename from Google will be "client_secret_{id}.json", but if you want to keep your scripts simple, the ServiceManager default looks for "google_client.json" in the "credentials" directory. Of course, these can be overriden and you can manually point to a client secret file.

    Notes:
        Services are cached by default. So, attempt to access the Sheets service from two different parts of an application will refer to the same service and service manager. This is done so you don't have to keep track of service manager objects in modules that are designed to be independent of each other, and, in most cases, this is the correct model because it ends up functioning like a singleton as only one user is authenticating to Google for a given execution. However, since there are potential needs to reference multiple paths, it can be explicitly instantiated to two different paths, in which you will need to balance multiple users, each connected to a separate service managers.
    '''
    api_key=None
    secret_file = 'google_client.json'
    credential_directory='credentials'
    oauth_args = []

    loaded_services = {}

    @classmethod
    def clear_class_services(cls):
        """ Uncache all services for this ServiceManager. """
        cls.loaded_services = {}

    def detach_services(self):
        """
        This will transfer the services from class variables to instance variables, for use with multiple ServiceManagers that point to different credentials. This has two purposes:
          1. It creates local services when the end developer doesn't want services pooled at the class level
          2. If there are already services previously loaded at the instance level, it clears them.
        """
        self.loaded_services = self.__class__.loaded_services.copy()

    def __init__(self,
                 services=None,
                 api_key=None,
                 secret_file=None,
                 credential_directory=None,
                 ):
        """
        Args:
            services (list, optional): A list of services to load up initially.
            api_key (str, optional): Uses the proivded developer API Key instead of OAUTH2 for authentication.
            secret_file (filename): The filename of the Google Developer OAUTH Credential File. By default, this is set to google_client.json. If no file exists, an exception is thrown on first attempt to authenticate.
            credential_directory (path): The path to the credential directory where the OATH credential file is and where service authorization tokens should be stored. By default, this is the credentials directory from wherever the program is being run. There are no built-in options to have a default  credential location because any guest would potentially be able to access all the user's Google data.
        """

        if api_key:
            self.api_key=api_key
        if credential_directory:
            self.credential_directory = credential_directory
        if secret_file:
            self.secret_file = secret_file
        if services:
            self.load_services(services)

    def load_services(self, service_keys):
        """ A proxy function to load a list of services instead of a single service. """
        for service in service_keys:
            self.load_service(service)

    def get_service(self, service_keys, load_if_invalid=False):
        """ Fetches *one* of the services requested, giving priority first to the existing cache or by loading them new. In most cases, this is handled by api-specific module.

        This is used to minimize new manual authorizations (or authorizations that exceed the necessary permissions) by fetching one of multiple permission scopes when a client API call can be called by multiple permissions scopes. For example, reading a description for an API object often can be done within a metadata scope, readonly scope, and full access scope. If no authorizations have been provided, we should load a service that only asks for metadata access, as it's the least intrusive. However, if the user has *already* authorized full access, there's no reason to launch a separate authentication window for the metadata scope, as it is entirely encompassed in full access.

        In the case a new authentication is required, the first service in the service_keys array is chosen as the scope. The user can change the order of the keys then to minimize authentications (e.g. listing full access before readonly access if their application will later be requiring full access).
        Args:
            service_keys (str|list): The list of valid service keys to search over.
            load_if_invalid (bool): Automatically load the first service in the service_keys list if no service currently exists. Default is False.
        Returns:
            A single, loaded service of the provided service_keys, or None if no services are found and load_if_invalid is False.
        """

        if type(service_keys) is not list:
            service_keys = [ service_keys ]

        for service_key in service_keys:
            if service_key in self.loaded_services:
                return(self.loaded_services[service_key])

        if load_if_invalid:
            return(self.load_service(service_keys[0]))
        else:
            return

    def load_service(self, api_name, api_version=None, permission_scope=None, force_refresh=False):
        """ Loads the requested service. If the service has already been loaded for this ServiceManager, return the previously loaded service (unless force_refresh is on). If it has not, delegate to get_credentials() as necessary.
        Args:
            api_name (str): The Google API name (i.e., 'drive.googleapis.com') or a shorthand version of it (e.g., 'drive').
            api_version (str, optional): The version of the API to use. If not provided, it will first check the DEFAULT_SCOPES mapping to determine if there is a default API. If not, it will attempt to use the directory service to determine the default API.
            permission_scope (str): The permission scope that accompanies this service. If the service_key is listed in the DEFAULT_SCOPES, this is optional and the default will be pulled. As fully-qualified permission scopes generally start with "https://www.googleapis.com/auth/", that part is optional and will be added if not present.
            force_refresh (bool): Reload the service even if it already has been loaded. Default is False.
        Returns:
            The loaded service.
        """
        #OLD and NEEDING TO DELETE: The fullly qualified service path, which also becomes the filename in the credential directory where the authorization token is stored. If not provided, this is generated from the service key ({service_key}.googleapis.com-python.json)

        if api_name in DEFAULT_SCOPES:
            keydata = DEFAULT_SCOPES[api_name]
            api_name = keydata[0]
            if not api_version:
                api_version = keydata[1]
            if not permission_scope:
                permission_scope = 'https://www.googleapis.com/auth/' + keydata[2]

        if not api_version:
            #TODO
            raise Exception("Pulling the discovery to determine the default version is not yet available")

        service_key = f"{api_name}.{api_version}"

        # Return the already-loaded service if it exists. This provides singleton-ish functionality at a Service:User level.
        if service_key in self.loaded_services and not force_refresh:
            return(self.loaded_services[service_key])

        # either service_key or service_path is required

        if self.api_key:
            # api keys should be used only for personal application and development
            # anyone with the api key can access Google services as the developer
            # TODO: This has not been tested in a while
            discovery = googleapiclient.discovery.build(api_name, api_version, developerKey=self.api_key)
        elif self.secret_file:
            # engage in OAuth2 authorization and credentialling

            service_path = f"{api_name}.{api_version}.googleapis.json"
            credentials = self.get_credentials(service_path, permission_scope)
            #authorizer = credentials.authorize(httplib2.Http())
            discovery = googleapiclient.discovery.build(api_name, api_version, credentials=credentials) #http=authorizer)
        else:
            raise Exception("Unable to load_service as no authentication models provided. Please specify an API Key or provide OAuth credentials to the googleapps.service.ServiceManager")

        # okay, save the service discovery for future calls
        self.loaded_services[service_key] = discovery
        return(self.loaded_services[service_key])


    def get_credentials(self, local_credential_file, permission_scope):
        """Gets valid user credentials - in most cases this is not required to be called directly and will be called from load_service().

        If nothing has been stored, or if the stored credentials are invalid, AND if application secret and scope are provided, the OAuth2 flow is completed to obtain the new credentials. This requires the user to authorize access via a web browser.

        Args:
            local_credential_file (path): the service-specific credential file, which is an authorization for this program/user to access these services. This file must exist in the credential_directory defined for this service object, or it will attempt to be fetched following user authorization. In the most common case where get_credentials is called by load_service(), this is determined in that function.
            permission_score (str): the permissions necessary for the application and that a remote call to authorize will request. The user may provide just the scope name (drive.readonly) or the full path to the permission scope (i.e. https://www.googleapis.com/auth/drive.readonly)

        Returns:
            Credentials, the obtained credential.
        """
        # auto create directory
        if not os.path.exists(self.credential_directory):
            os.makedirs(self.credential_directory)

        # convert the shorthand permission scope to the full path
        if not re.match('https', permission_scope):
            permission_scope = 'https://www.googleapis.com/auth/' + permission_scope


        # determine ifr the credentials have already been authorized and are active
        credential_path = os.path.join(self.credential_directory, local_credential_file)
        if os.path.exists(credential_path):
            credentials = google.oauth2.credentials.Credentials.from_authorized_user_file(credential_path, permission_scope)
        else:
            credentials = None

        if credentials and credentials.valid and credentials.expired and credentials.refresh_token:
            # creds exist and arre valid, but are expired - so just refresh
            credentials.refresh(google.auth.transport.requests.Request())
        else:
            # no credientials, or they are invalid!
            # -- get new credentials
            # identify the path to the credential's secret file.
            secret_path = os.path.join(self.credential_directory, self.secret_file)

            # a very detailed error message.
            if not os.path.exists(secret_path):
                raise FileNotFoundError(f"Could not find an OAuth secret file at {secret_path}, which is required for ServiceManager.get_credentials() to attempt to complete the authorization permission for scope {permission_scope} (the scope-level permission should be stored in {local_credential_file}, but it does not exist or is no longer valid and needs to be authenticated). \n\nYou will need to indicate the correct path to your OAuth Credential JSON secret file or download a new copy from the Google Developers Console located at https://console.developers.google.com/apis/credentials/ before trying again.")

            # All set authorize flow.
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(secret_path, permission_scope)
                credentials = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(credential_path, 'w') as token:
            token.write(credentials.to_json())

        return(credentials)
