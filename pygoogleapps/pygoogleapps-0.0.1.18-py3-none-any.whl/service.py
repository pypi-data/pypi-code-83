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
import os
import datetime
import re
import shutil

import warnings
from pprint import pprint

import httplib2

import oauth2client
import oauth2client.file
import oauth2client.tools

import googleapiclient # to install this : pip install --upgrade google-api-python-client
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
    'gmail': ['gmail', 'v1', 'gmail.compose'],
    'sheets': ['sheets', 'v4', 'spreadsheets'],
    'sheets.readonly': ['sheets', 'v4', 'spreadsheets.readonly'],
    'drive': ['drive', 'v3', 'drive'],
    'drive.metadata': ['drive', 'v3', 'drive.metadata'],
    'drive.readonly': ['drive', 'v3', 'drive.readonly'],
    'docs': ['docs', 'v1', 'documents'],
}

class ServiceManager(object):
    '''
    The ServiceManager is intended to encapsulate all of the Google services for a user. The SM object must be tied to the registered OAUTH secret file, which the user must download from the Google Developer Console (https://console.developers.google.com/apis/credentials). The filename from Google will be "client_secret_{ids}.json", but the ServiceManager default looks for "google_client.json" in the "credentials" directory, but these can be overriden.

    Notes:
        Services are cached so that a reference to a Sheets service from two different parts of an application refer to the same service and service manager. In most cases, it ends up functioning like a singleton as only one user is likely to be authenticating to Google for a given script. But since there are plenty of potential needs to reference multiple paths, it can be explicitly instantiated to two different paths.
    '''
    api_key=None
    oauth_secret_file = 'google_client.json'
    oauth_credential_directory='credentials'
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
                 oauth_secret_file=None,
                 oauth_credential_directory=None,
                 ):
        """
        Args:
            services (list, optional): A list of services to load up initially.
            api_key (str, optional): Uses the proivded developer API Key instead of OAUTH2 for authentication.
            oauth_secret_file (filename): The filename of the Google Developer OAUTH Credential File. By default, this is set to google_client.json. If no file exists, an exception is thrown on first attempt to authenticate.
            oauth_credential_directory (path): The path to the credential directory where the OATH credential file is and where service authorization tokens should be stored. By default, this is the credentials directory from wherever the program is being run. There are no built-in options to have a default  credential location because any guest would potentially be able to access all the user's Google data.
        """

        if api_key:
            self.api_key=api_key
        if oauth_credential_directory:
            self.oauth_credential_directory = oauth_credential_directory
        if oauth_secret_file:
            self.oauth_secret_file = oauth_secret_file
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

    def load_service(self, service_key=None, version=None, service_path=None, permission_scope=None, force_refresh=False):
        """ Loads the requested service. If the service has already been loaded for this ServiceManager, return the previously loaded service (unless force_refresh is on). If it has not, delegate to get_credentials() as necessary.
        Args:
            service_key (str): The service key, which may be a shorthand value ('drive') or a qualified google api path ('drive.googleapis.com'). If not provided, the service key will be pulled from the first part of the service_path string.
            version (str): The version of the API
            service_path (str): The fullly qualified service path, which also becomes the filename in the credential directory where the authorization token is stored. If not provided, this is generated from the service key ({service_key}.googleapis.com-python.json)
            permission_scope (str): The permission scope that accompanies this service. If the service_key is listed in the DEFAULT_SCOPES, this is optional and the default will be pulled.
            force_refresh (bool): Reload the service even if it already has been loaded. Default is False.
        Returns:
            The loaded service.
        """

        # only actually load if it needs to be
        if service_key in self.loaded_services and not force_refresh:
            return self.loaded_services[service_key]

        # either service_key or service_path is required
        if not service_key:
            if service_path:
                match = re.match('(.*)\.googleapis', service_path)
                service_key = match.group(1)
            else:
                raise Exception("load_services() requires either the service_key or the service_path to be provided")

        # determine
        if service_key in DEFAULT_SCOPES:
            keydata = DEFAULT_SCOPES[service_key]
            api_name = keydata[0]
            version = keydata[1]
            if not permission_scope:
                permission_scope = 'https://www.googleapis.com/auth/' + keydata[2]

        if self.api_key:
            # api keys should be used only for personal application and development
            # anyone with the api key can access Google services as the developer
            discovery = googleapiclient.discovery.build(api_name, version, developerKey=self.api_key)
        elif self.oauth_secret_file:
            # engage in OAuth2 authorization and credentialling

            service_path = service_key + '.googleapis.com-python.json'

            # convert the shorthand permission scope to the full path
            if not re.match('https', permission_scope):
                permission_scope = 'https://www.googleapis.com/auth/' + permission_scope

            credentials = self.get_credentials(service_path, permission_scope)
            authorizer = credentials.authorize(httplib2.Http())
            discovery = googleapiclient.discovery.build(api_name, version, http=authorizer)
        else:
            raise Exception("Unable to load_service as no authentication models provided. Please specify an API Key or provide OAuth credentials to the googleapps.service.ServiceManager")

        # okay, save the service discovery for future calls
        self.loaded_services[service_key] = discovery
        return(self.loaded_services[service_key])


    def get_credentials(self, local_credential_file, permission_scope=None):
        """Gets valid user credentials - in most cases this is not required to be called directly and will be called from load_service().

        If nothing has been stored, or if the stored credentials are invalid, AND if application secret and scope are provided, the OAuth2 flow is completed to obtain the new credentials. This requires the user to authorize access via a web browser.

        Args:
            local_credential_file (path): the service-specific credential file, which is an authorization for this program/user to access these services. This file must exist in the oauth_credential_directory defined for this service object, or it will attempt to be fetched following user authorization. In the most common case where get_credentials is called by load_service(), this is determined in that function.
            permission_score (str): the permissions necessary for the application and that a remote call to authorize will request. The user may provide just the scope name (drive.readonly) or the full path to the permission scope (i.e. https://www.googleapis.com/auth/drive.readonly)

        Returns:
            Credentials, the obtained credential.
        """

        # auto create directory
        if not os.path.exists(self.oauth_credential_directory):
            os.makedirs(self.oauth_credential_directory)

        credential_path = os.path.join(self.oauth_credential_directory, local_credential_file)
        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()

        if not credentials or credentials.invalid :
            if not permission_scope:
                raise Exception("No permission scope provided to get_credentials() called for " + local_credential_file + ", which does not exist or is not valid and needs to be authenticated.")

            # identify the path to the credential's secret file.
            oauth_secret_path = os.path.join(self.oauth_credential_directory, self.oauth_secret_file)

            # a very detailed error message.
            if not os.path.exists(oauth_secret_path):
                raise FileNotFoundError(f"Could not find an OAuth secret file at {oauth_secret_path}, which is required for ServiceManager.get_credentials() to attempt to complete the authorization permission for scope {permission_scope} (the scope-level permission should be stored in {local_credential_file}, but it does not exist or is no longer valid and needs to be authenticated). \n\nYou will need to indicate the correct path to your OAuth Credential JSON secret file or download a new copy from the Google Developers Console located at https://console.developers.google.com/apis/credentials/ before trying again.")

            # All set.
            # Do OAuth authentication
            if not re.match('https', permission_scope):
                permission_scope = 'https://www.googleapis.com/auth/' + permission_scope

            # to date, I've never set any oauth args.
            #flags = oauth2client.tools.argparser.parse_args(args=self.oauth_args)
            flow = oauth2client.client.flow_from_clientsecrets(
                oauth_secret_path,
                permission_scope
            )
            #if flags:
            #    credentials = oauth2client.tools.run_flow(flow, store, flags)
            #else:
            credentials = oauth2client.tools.run_flow(flow, store)
        return(credentials)
