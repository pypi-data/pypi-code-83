import logging

from modules.torch.initialiser import torch_client_credentials
from modules.torch.models.pipeline import CreatePipeline, PipelineMetadata
from modules.torch.torch_client import TorchClient

logging.basicConfig(level=logging.INFO)

# Set up torch client
torchClient = TorchClient(**torch_client_credentials)

# create pipeline object
pipeline = CreatePipeline(
    uid='monthly_reporting-39',
    name='Monthly reporting Pipeline-39',
    description='Pipeline to create monthly reporting tables',
    meta=PipelineMetadata('vaishvik', 'torch', '...'),
    context={'key1': 'value1'}
)
# creating pipeline using torch client
pipelineResponse = torchClient.create_pipeline(pipeline=pipeline)
print('Newly Created Pipeline Response : ', pipelineResponse)

# create a pipeline run of the pipeline
pipelineRunResponse = pipelineResponse.create_pipeline_run(context_data={'team': 'torch', 'name': 'backend'})
print('pipeline Run Created :', pipelineRunResponse)

# create span in the pipeline run
spanContext = pipelineRunResponse.create_span(uid='span_uid_39_1',
                                              context_data={'start': 'tuesday', 'name': 'vaishvik'})
print('Span Created :', spanContext)

# check current span is root or not
print('span is root or not : ', spanContext.is_root())

# end the span event
print('Span End Event Response :', spanContext.end())

# check if the current span has children or not
print('has child ', spanContext.has_children())

# create a child span
childSpanContext = spanContext.create_child_span('span_uid_39_2')
print('child span is root or not  ', childSpanContext.is_root())
print('child span abort event : ', childSpanContext.abort())

print('child span has child or not : ', childSpanContext.has_children())
print('parent span has child or not : ', spanContext.has_children())
