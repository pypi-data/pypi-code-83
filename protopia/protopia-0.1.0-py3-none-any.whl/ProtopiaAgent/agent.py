import grpc
import os
import sys
from .protopia.api.noise.v1beta1.distribution_pb2 import GetNoiseDistributionRequest
from .protopia.api.noise.v1beta1.distribution_pb2_grpc import NoiseStub
from .grpc_auth.jwt import JwtAuthMetadataPlugin

MAX_MESSAGE_LENGTH = 20 * 1024 * 1024
PROTOPIA_CLOUD_STAGE_URL = 'api.stage-01.stage.protopia.ai:443'
STAGE_TOKEN_URL = 'https://protopia-cloud-stage-01.auth.us-east-1.amazoncognito.com/oauth2/token'
SCOPES = ['https://api.stage-01.protopia.ai/noise:read']

class Agent:
    """
    Note, the following variables must be set prior to calling this method:
    - OIDC_CLIENT_ID: the OAuth2 client_id.
    - OIDC_CLIENT_SECRET: the OAuth2 client_secret.
    """
    def __init__(self) -> None:
        self.MAX_MESSAGE_LENGTH = 20 * 1024 * 1024
        self.PROTOPIA_CLOUD_URL = 'api.stage-01.stage.protopia.ai:443'
        self.TOKEN_URL = 'https://protopia-cloud-stage-01.auth.us-east-1.amazoncognito.com/oauth2/token'
        self.SCOPES = ['https://api.stage-01.protopia.ai/noise:read']

        self.OIDC_CLIENT_ID = None
        self.OIDC_CLIENT_SECRET = None

        self.channel = None

    def set_url(self, url):
        self.PROTOPIA_CLOUD_URL = url
        print("PROTOPIA_CLOUD_URL is set to " + url)

    def set_token_url(self, token_url):
        self.TOKEN_URL = token_url
        print("TOKEN_URL is set to " + token_url)

    def set_scopes(self, scopes):
        self.SCOPES = scopes
        print("SCOPES is set to " + scopes)

    def set_client(self, id, secret):
        self.OIDC_CLIENT_ID = id
        self.OIDC_CLIENT_SECRET = secret
        print("OIDC_CLIENT_ID is set to " + id)
        print("OIDC_CLIENT_SECRET is set to " + secret)

    def set_option(self, option_dict):
        for k, v in option_dict.items():
            self[k] = v
            print(k + " is set to " + v)

    def get_option(self):
        print("PROTOPIA_CLOUD_URL is set to " + self.PROTOPIA_CLOUD_URL)
        print("TOKEN_URL is set to " + self.TOKEN_URL)
        print("SCOPES is set to " + str(self.SCOPES))
        print("OIDC_CLIENT_ID is set to " + str(self.OIDC_CLIENT_ID))
        print("OIDC_CLIENT_SECRET is set to " + str(self.OIDC_CLIENT_SECRET))

    def connect(self):
        if self.OIDC_CLIENT_ID is None or self.OIDC_CLIENT_SECRET is None:
            raise ValueError('OIDC_CLIENT_ID and OIDC_CLIENT_SECRET environment variables must be specified')

        ssl = grpc.ssl_channel_credentials()
        jwt_auth_plugin = JwtAuthMetadataPlugin(self.OIDC_CLIENT_ID, self.OIDC_CLIENT_SECRET, self.TOKEN_URL, self.SCOPES)
        jwt_auth = grpc.metadata_call_credentials(jwt_auth_plugin)
        credentials = grpc.composite_channel_credentials(ssl, jwt_auth)

        self.channel = grpc.secure_channel(PROTOPIA_CLOUD_STAGE_URL, credentials, options=[
            ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
            ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)
        ])
        print('successfully connected to staging cloud API')

    def get_noise_distribution(self, nnid):
        """Connects to Protopia Cloud API over SSL protocol authorized by JWT tokens and downloads a noise distribution.
        """

        if self.channel is None:
            self.connect()

        client = NoiseStub(self.channel)

        if nnid is None:
            raise ValueError("nnid must be specified")

        request = GetNoiseDistributionRequest(nnid=nnid)
        try:
            distribution = client.GetNoiseDistribution(request)
            print('successfully retrieved encrypted noise distribution\n', distribution)
            return distribution

        except grpc.RpcError as e:
            print('failed to retrieve noise distribution, caused by:', e)

if __name__ == '__main__':
    client = Agent()