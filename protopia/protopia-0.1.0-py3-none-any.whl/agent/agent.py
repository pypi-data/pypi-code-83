import grpc
import os
import sys
from protopia.api.noise.v1beta1.distribution_pb2 import GetNoiseDistributionRequest
from protopia.api.noise.v1beta1.distribution_pb2_grpc import NoiseStub
from grpc_auth.jwt import JwtAuthMetadataPlugin

MAX_MESSAGE_LENGTH = 20 * 1024 * 1024
PROTOPIA_CLOUD_STAGE_URL = 'api.stage-01.stage.protopia.ai:443'
STAGE_TOKEN_URL = 'https://protopia-cloud-stage-01.auth.us-east-1.amazoncognito.com/oauth2/token'
SCOPES = ['https://api.stage-01.protopia.ai/noise:read']


def connect_original():
    """Connects to Protopia Cloud API over SSL protocol authorized by JWT tokens and downloads a noise distribution.
       Note, the following environment variables must be set prior to calling this method:
       - OIDC_CLIENT_ID: the OAuth2 client_id.
       - OIDC_CLIENT_SECRET: the OAuth2 client_secret.
    """
    client_id = os.getenv("OIDC_CLIENT_ID")
    client_secret = os.getenv("OIDC_CLIENT_SECRET")

    if client_id is None or client_secret is None:
        sys.exit('OIDC_CLIENT_ID and OIDC_CLIENT_SECRET environment variables must be specified')

    ssl = grpc.ssl_channel_credentials()
    jwt_auth_plugin = JwtAuthMetadataPlugin(client_id, client_secret, STAGE_TOKEN_URL, SCOPES)
    jwt_auth = grpc.metadata_call_credentials(jwt_auth_plugin)
    credentials = grpc.composite_channel_credentials(ssl, jwt_auth)

    channel = grpc.secure_channel(PROTOPIA_CLOUD_STAGE_URL, credentials, options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)
    ])
    print('successfully connected to staging cloud API')
    client = NoiseStub(channel)
    request = GetNoiseDistributionRequest(nnid='0000')
    try:
        distribution = client.GetNoiseDistribution(request)
        print('successfully retrieved encrypted noise distribution\n', distribution)
    except grpc.RpcError as e:
        print('failed to retrieve noise distribution, caused by:', e)

def connect(client_id, client_secret):
    """Connects to Protopia Cloud API over SSL protocol authorized by JWT tokens and downloads a noise distribution.
       Note, the following environment variables must be set prior to calling this method:
       - OIDC_CLIENT_ID: the OAuth2 client_id.
       - OIDC_CLIENT_SECRET: the OAuth2 client_secret.
    """

    if client_id is None or client_secret is None:
        sys.exit('OIDC_CLIENT_ID and OIDC_CLIENT_SECRET environment variables must be specified')

    ssl = grpc.ssl_channel_credentials()
    jwt_auth_plugin = JwtAuthMetadataPlugin(client_id, client_secret, STAGE_TOKEN_URL, SCOPES)
    jwt_auth = grpc.metadata_call_credentials(jwt_auth_plugin)
    credentials = grpc.composite_channel_credentials(ssl, jwt_auth)

    channel = grpc.secure_channel(PROTOPIA_CLOUD_STAGE_URL, credentials, options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)
    ])
    print('successfully connected to staging cloud API')
    client = NoiseStub(channel)
    request = GetNoiseDistributionRequest(nnid='0000')
    try:
        distribution = client.GetNoiseDistribution(request)
        print('successfully retrieved encrypted noise distribution\n', distribution)
    except grpc.RpcError as e:
        print('failed to retrieve noise distribution, caused by:', e)

if __name__ == '__main__':
    connect()
