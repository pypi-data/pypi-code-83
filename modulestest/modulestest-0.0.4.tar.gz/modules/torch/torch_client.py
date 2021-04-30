from modules.torch.models.pipeline import CreatePipeline
from modules.torch.torch_http_client import TorchHttpClient
from modules.torch.models.datasource import CreateDataSource


class TorchClient:

    def __init__(self, url, timeout_ms=10000, access_key: str = None, secret_key: str = None):
        """
                Description : Torch user client is used to send data to catalog server.

                :param url: (String) url of the catalog server
                :param timeout_ms: (Integer) timeout of the requests sending to catalog
                :param access_key: (String) Access key of API key. You can generate API key from torch UI's setting
                :param secret_key: (String) Secret key of API key.

                Ex.  TorchClient = TorchUserClient(url='https://torch.acceldata.local:5443', access_key='OY2VVIN2N6LJ', secret_key='da6bDBimQfXSMsyyhlPVJJfk7Zc2gs')
        """

        if access_key is None and secret_key is None:
            raise Exception('Access key and secret key - required')
        self.client = TorchHttpClient(url=url, access_key=access_key, secret_key=secret_key, timeout_ms=timeout_ms)

    def create_pipeline(self, pipeline: CreatePipeline):
        """
            Description:
                To create pipeline in torch catalog service
        :param pipeline: (CreatePipeline) class instance of the pipeline to be created
        :return: (Pipeline) newly created pipeline class instance
        """
        if pipeline.uid is None or pipeline.name is None:
            raise Exception('To create a pipeline, pipeline uid/name is required')
        return self.client.create_pipeline(pipeline)

    def get_pipeline(self, uid: str):
        """
            Description:
                To get an existing pipeline from torch catalog
        :param uid: uid of the pipeline
        :return:(Pipeline) pipeline class instance
        """
        if uid is None:
            raise Exception('To get a pipeline, pipeline uid is required')
        return self.client.get_pipeline(uid)

    def create_datasource(self, datasource: CreateDataSource):
        """"
            Description:
                To create datasource in torch catalog
        :param datasource: (CreateDataSource) class instance of the datasource to be created
        :return: (DataSource) newly created datasource
        """
        return self.client.create_datasource(datasource)

    def get_datasource(self, name: str):
        """
        Description:
            Find datasource by it's name in torch catalog
        :param name: name of the datasource given in torch
        :return: (DataSource) datasource
        """
        return self.client.get_datasource(name)

    def get_asset_types(self):
        """
        Description:
            get all asset types supported in torch catalog
        :return: list of asset types
        """
        return self.client.get_all_asset_types()

    def get_all_source_types(self):
        """
        Description:
            get all source types supported in torch catalog
        :return: list of all source type
        """
        return self.client.get_all_source_types()
