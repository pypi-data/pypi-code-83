from torchsdktest.models.pipeline import CreatePipeline, PipelineMetadata
from torchsdktest.torch_client import TorchClient


# setup pipeline in torch catalog
def setup_torch_pipeline():
    torchClient = TorchClient(url="https://torch.acceldata.local:5443", access_key="OY2VVIN2N6LJ",
                              secret_key="da6bDBimQfXSMsyyhlPVJJfk7Zc2gs")

    # create pipeline object
    pipeline = CreatePipeline(
        uid='monthly_reporting-test',
        name='Monthly reporting Pipeline-test',
        description='Pipeline to create monthly reporting tables',
        meta=PipelineMetadata('Vaishvik', 'torch', '...'),
        context={'key1': 'value1'}
    )

    # creating pipeline using torch client
    pipeline_response = torchClient.create_pipeline(pipeline=pipeline)
    print('Torch Pipeline created successfully. ')

    # create a pipeline run of the pipeline
    pipeline_run = pipeline_response.create_pipeline_run(context_data={'key1': 'value2', 'name': 'backend'})
    print('pipeline Run Created Successfully. ')
    return pipeline_run


# get latest pipeline run
def get_pipeline_run():
    torchClient = TorchClient(url="https://torch.acceldata.local:5443", access_key="OY2VVIN2N6LJ",
                              secret_key="da6bDBimQfXSMsyyhlPVJJfk7Zc2gs")
    pipeline = torchClient.get_pipeline('monthly_reporting-test')
    pipeline_run = pipeline.get_latest_pipeline_run()
    print('latest pipeline run : ', pipeline_run)
    return pipeline_run
