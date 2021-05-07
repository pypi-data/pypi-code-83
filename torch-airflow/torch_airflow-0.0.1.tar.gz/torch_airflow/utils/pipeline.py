from torch_airflow.initialiser import torch_credentials
from torchsdktest.torch_client import TorchClient


def create_pipeline_run(pipeline_uid, context_data=None):
    torchClient = TorchClient(**torch_credentials)
    pipeline = torchClient.get_pipeline(pipeline_uid)
    pipeline_run = pipeline.create_pipeline_run(context_data=context_data)
    return pipeline_run


def get_latest_pipeline_run(pipeline_uid):
    torchClient = TorchClient(**torch_credentials)
    pipeline = torchClient.get_pipeline(pipeline_uid)
    pipeline_run = pipeline.get_latest_pipeline_run()
    return pipeline_run
