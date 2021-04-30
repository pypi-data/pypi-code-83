import json
import time
from urllib.parse import urlencode
import jwt
import requests

class AdobeIO:
    def __init__(self,JWT_PAYLOAD,PRIVATE_KEY_PATH,CLIENT_SECRET):
        self.ORG_ID = JWT_PAYLOAD["iss"]
        self.ACCNT_ID = JWT_PAYLOAD["sub"]
        self.API_KEY =JWT_PAYLOAD["aud"].split('/')[-1]
        self.IMS_HOST="https://"+JWT_PAYLOAD["aud"].split('/')[2]
        for x in JWT_PAYLOAD:
            if JWT_PAYLOAD[x]==True:
                self.API_PATH = x
        self.PRIVATE_KEY_PATH = PRIVATE_KEY_PATH
        self.CLIENT_SECRET = CLIENT_SECRET
        self.jwt_token = ""
        self.access_token=""

    def generate_jwt(self):
        #expiry time as 24 hours
        expiry_time_jwt = int(time.time()) + 60 * 60 * 24
        # create payload
        payload = {
            'exp': expiry_time_jwt,
            'iss': self.ORG_ID,
            'sub': self.ACCNT_ID,
            self.API_PATH: True,
            'aud': self.IMS_HOST + "/c/" + self.API_KEY
        }
        # read the private key we will use to sign the JWT.
        priv_key_file = open(self.PRIVATE_KEY_PATH)
        priv_key = priv_key_file.read()
        priv_key_file.close()
        # create JSON Web Token, signing it with the private key.
        jwt_token = jwt.encode(payload, priv_key, algorithm='RS256')
        self.jwt_token = jwt_token
        return jwt_token

    def generate_access_token(self):
        access_token = ''

        # Final URL for access-token generation API end-point
        accesstoken_url =  self.IMS_HOST + "/ims/exchange/jwt/"

        accesstoken_headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache"
        }

        accesstoken_body_credentials = {
            "client_id": self.API_KEY,
            "client_secret": self.CLIENT_SECRET,
            "jwt_token": self.jwt_token
        }

        accesstoken_body = urlencode(accesstoken_body_credentials)
        # send http request
        print(accesstoken_body)
        print(accesstoken_url)
        res = requests.post(accesstoken_url, headers=accesstoken_headers, data=accesstoken_body)

        if res.status_code == 200:
            # extract token
            access_token = json.loads(res.text)['access_token']
        self.access_token = access_token
        return access_token

class AAM(AdobeIO):
    def __init__(self, JWT_PAYLOAD,PRIVATE_KEY_PATH,CLIENT_SECRET):
        AdobeIO.__init__(self, JWT_PAYLOAD,PRIVATE_KEY_PATH,CLIENT_SECRET)
        self.datasourceendpoint = "https://api.demdex.com/v1/datasources/"
        self.traitsendpoint = "https://api.demdex.com/v1/traits/"
        self.traitfoldersendpoint = "https://api.demdex.com/v1/folders/traits/"
        self.segmentsendpoint = "https://api.demdex.com/v1/segments/"
        self.segmentfoldersendpoint = "https://api.demdex.com/v1/folders/segments/"
        self.destinationsendpoint = "https://api.demdex.com/v1/destinations/"


    def auth_header(self):
        return {
            "x-api-key":self.API_KEY,
            "content-type": "application/json",
            "accept": "application/json",
            "Authorization": "Bearer "+self.access_token
        }

    def get_datasource(self,params):
        return requests.get(self.datasourceendpoint,headers=self.auth_header(),params=params)

    def get_traits(self,params=None):
        print(params)
        return requests.get(self.traitsendpoint,headers=self.auth_header(),params=params)

    def create_traits(self,data=None):
        if data is None:
            return None
        else:
            return requests.post(self.traitsendpoint,headers=self.auth_header(),data=data)

    def create_segments(self,data=None):
        if data is None:
            return None
        else:
            return requests.post(self.segmentsendpoint,headers=self.auth_header(),data=json.dumps(data))

    def update_segments(self,data=None,segmentId=None):
        if data is None or segmentId is None:
            return None
        else:
            return requests.put(self.segmentsendpoint+str(segmentId)+"/",headers=self.auth_header(),data=json.dumps(data))

    def get_segments(self,params=None):
        return requests.get(self.segmentsendpoint,headers=self.auth_header(),params=params)

    def get_segment_folders(self,params=None):
        return requests.get(self.segmentfoldersendpoint,headers=self.auth_header(),params=params)

    def get_trait_folders(self,params=None):
        return requests.get(self.traitfoldersendpoint,headers=self.auth_header(),params=params)

    def get_destinations(self,params=None):
        return requests.get(self.destinationsendpoint,headers=self.auth_header(),params=params)

    def get_destination_mappings(self,params=None,destinationId=None):
        if destinationId!=None:
            return requests.get(self.destinationsendpoint+str(destinationId)+"/mappings/",headers=self.auth_header(),params=params)
        else:
            return None

    def set_destination_mappings(self,data=None,destinationId=None):
        if data is None or destinationId is None:
            return None
        else:
            return requests.post(self.destinationsendpoint+str(destinationId)+"/mappings/",headers=self.auth_header(),data=json.dumps(data))

class AA(AdobeIO):
    def __init__(self, JWT_PAYLOAD,PRIVATE_KEY_PATH,CLIENT_SECRET,COMPANY_ID):
        AdobeIO.__init__(self, JWT_PAYLOAD,PRIVATE_KEY_PATH,CLIENT_SECRET)
        self.reportingendpoint = "https://api.demdex.com/v1/datasources/"
        self.companyid = COMPANY_ID
        #Nikhil to update
    def get_reports(self,params=None):
        return requests.get(self.segmentsendpoint,headers=self.auth_header(),params=params)

class AATriggers():
    def __init__(self,postCallBack=None,ngrok=False):
        self.postCallBack = postCallBack



