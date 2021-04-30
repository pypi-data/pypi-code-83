from torch.initialiser import torchClientCredentials
from torch.models.job import CreateJob, Dataset, JobMetadata
from torch.models.pipeline import CreatePipeline, PipelineMetadata
from torch.torch_user_client import TorchUserClient
import logging
logging.basicConfig(level=logging.INFO)

torchClient = TorchUserClient(**torchClientCredentials)
createPipeline = CreatePipeline(
    uid='monthly_reporting-37',
    name='Monthly reporting Pipeline-37',
    description='Pipeline to create monthly reporting tables',
    meta=PipelineMetadata('vaishvik', 'torch', '...'),
    context={'key1': 'value1'}
)
pipelineResponse = torchClient.createPipeline(pipeline=createPipeline)
print(pipelineResponse)

createJob = CreateJob(
    uid='monthly_sales_aggregate-37',
    name='Monthly Sales Aggregate-37',
    description='Generates the monthly sales aggregate tables for the complete year',
    inputs=[Dataset('postgres-assembly-5450', 'ad_catalog.ad_catalog.flyway_schema_history')],
    outputs=[Dataset('postgres-ds', 'ad_catalog.ad_catalog.flyway_schema_history')],
    meta=JobMetadata('vaishvik', 'backend', 'https://github.com/acme/reporting/reporting.scala'),
    context={'key21': 'value21'}
)
# job creation
jobResponse = pipelineResponse.createJob(createJob)
print(jobResponse)

# pipelinerun creation
pipelineRunRes = pipelineResponse.createPipelineRun(pipelineRunArgs={'key1': 'value2', 'name': 'backend'})
print('pipeline run created :: output ::', pipelineRunRes)

# update pipelinerun
updatePipelineRunRes = pipelineRunRes.updatePipelineRun(pipelineRunArgs={'key1':'value2', 'name': 'backend'})
print('pipeline run updated :: output ::',updatePipelineRunRes)

# create span
createSpanRes = pipelineRunRes.createSpan(spanUid='span_uid_37')
print('span created :: output: ', createSpanRes)

print(createSpanRes.start({'k': 'v'}))
print('root ', createSpanRes.isRoot())
print('log event .', createSpanRes.sendLogs(contextData={'k': 'v'}, logData='this is log data for a event'))
print('log event .', createSpanRes.sendCustomEvent(eventType='CUSTOM_EVENT', contextData={'k': 'v'}))
print(createSpanRes.end())
print('has child ', createSpanRes.hasChildren())

print('new child span : creating...............................................................................')
childSpanRes = createSpanRes.createChildSpan('span_uid_37_2')
print(childSpanRes.start())
print('root ', childSpanRes.isRoot())
print(childSpanRes.abort())
print('has children ............ span checking')
print('child span hasChild ', childSpanRes.hasChildren())
print('parent -> has child ', createSpanRes.hasChildren())
