from modules.torch.models.asset import CreateAsset, CreateAssetRelation, RelationType, AssetMetadata
from modules.torch.models.datasource import CreateDataSource, SourceType
from modules.torch.models.job import CreateJob, Dataset, JobMetadata
from modules.torch.models.pipeline import CreatePipeline, PipelineMetadata, PipelineRun
from modules.torch.models.snapshot import SnapshotData, AssociatedItemType
from modules.torch.models.span import Span, CreateSpanEvent
from modules.torch.models.span_context import SpanContext
from torch_client import TorchHttpClient

TorchClient = TorchHttpClient(url='https://torch.acceldata.local:5443', access_key='OY2VVIN2N6LJ',
                          secret_key='da6bDBimQfXSMsyyhlPVJJfk7Zc2gs')

# TorchClient = torchClientInstance
createPipeline = CreatePipeline(
    uid='monthly_reporting-36',
    name='Monthly reporting Pipeline-36',
    description='Pipeline to create monthly reporting tables',
    meta=PipelineMetadata('vaishvik', 'torch', '...'),
    context={'key1': 'value1'}
)
pipelineResponse = TorchClient.createPipeline(pipeline=createPipeline)
print(pipelineResponse)

createJob = CreateJob(
    uid='monthly_sales_aggregate-36',
    name='Monthly Sales Aggregate-36',
    description='Generates the monthly sales aggregate tables for the complete year',
    inputs=[Dataset('postgres-assembly-5450', 'ad_catalog.ad_catalog.flyway_schema_history')],
    outputs=[Dataset('postgres-ds', 'ad_catalog.ad_catalog.flyway_schema_history')],
    meta=JobMetadata('vaishvik', 'backend', 'https://github.com/acme/reporting/reporting.scala'),
    context={'key21': 'value21'}
)
# job creation
# jobResponse = pipelineResponse.createJob(createJob)
# print(jobResponse)

# pipelinerun creation
pipelineRunRes = pipelineResponse.createPipelineRun(pipelineRunArgs={'key1': 'value2', 'name': 'backend'})
print('pipeline run created :: output ::', pipelineRunRes)

# update pipelinerun
# updatePipelineRunRes = pipelineRunRes.updatePipelineRun(pipelineRunArgs={'key1':'value2', 'name': 'backend'})
# print('pipeline run updated :: output ::',updatePipelineRunRes)

# create span
createSpanRes = pipelineRunRes.createSpan(spanUid='span_uid_36')
print('span created :: output: ', createSpanRes)

# print(createSpanRes.start({'k': 'v'}))
# print('root ', createSpanRes.isRoot())
# print('log event .', createSpanRes.sendLogs(contextData={'k': 'v'}, logData='this is log data for a event'))
# print('log event .', createSpanRes.sendCustomEvent(eventType='CUSTOM_EVENT', contextData={'k': 'v'}))
# print(createSpanRes.end())
#
# print('has child ', createSpanRes.hasChildren())
# # print('new child span : creating...............................................................................')
# childSpanRes = createSpanRes.createChildSpan('span_uid_36_2')
# print(childSpanRes.start())
# print('root ', childSpanRes.isRoot())
# print(childSpanRes.abort())
# print('has children ............ span checking')
# print('child span hasChild ', childSpanRes.hasChildren())
# print('parent -> has child ', createSpanRes.hasChildren())

# resJob = TorchClient.createJob(job=createJob)
# print(resJob)

createPipelineRun = PipelineRun(
    pipelineId=30,
    pipelineSnapshotId='cb1e4fcb-5c1c-4f44-8b46-d395d83f316f',
    args={'k1': 'v2', 'k3': 'v3'}
)

# createPipelineRunRes = TorchClient.createPipelineRun(createPipelineRun)
# print(createPipelineRunRes)

updatePipelineRun = PipelineRun(
    pipelineId=30,
    pipelineSnapshotId='cb1e4fcb-5c1c-4f44-8b46-d395d83f316f',
    args={'k1': 'vl2', 'k3': 'vl1'},
)
# updatePipelineRunRes = TorchClient.updatePipelineRun(2,updatePipelineRun)
# print(updatePipelineRunRes)

datasource = CreateDataSource(
    name='Feature_bag_datasource_new_6',
    sourceType=SourceType(21, 'FEATURE_BAG'),
    description='feature bag assembly creation using python sdk',
    # name= 'aws_athena_ds_sdk',
    # sourceType= SourceType(16, 'AWS_ATHENA'),
    # description= 'creation of assembly using sdk',

    isVirtual=True,
    # connectionId= 1,
    # configProperties= [ ConfigProperty(key= 's3.location', value= 's3://ad-redshift-data/athena_result/vaishvik')]
)

# resds = TorchClient.createDataSource(datasource)
# print(resds)


# # dsRes =  {'data': {'assemblyProperties': None, 'configuration': {'schedule': {'cron': None, 'enabled': False}}, 'conn': None, 'connectionId': None, 'crawler': {'name': 'feature_bag'}, 'createdAt': '2021-04-12T17:15:39.950+05:30', 'currentSnapshot': None, 'description': 'feature bag assembly creation using python sdk', 'id': 18, 'isSecured': False, 'isVirtual': True, 'name': 'Feature_bag_datasource', 'schedule': None, 'securityConfig': None, 'sourceType': {'connectionTypeId': None, 'id': 21, 'name': 'FEATURE_BAG', 'sourceModel': {'id': 6, 'name': 'ML'}}, 'updatedAt': '2021-04-12T17:15:39.950+05:30'}}
# # print(dsRes)
# # res = TorchClient.convertDictToDatasource(dsRes).crawler
# # print(res)

asset = CreateAsset(
    name='feature_26',
    description='feature number 26',
    assemblyId=20,
    uid='Feature_bag_datasource_temp.feature26',
    assetTypeId=22,
    sourceTypeId=21,
    isCustom=False,
    # parentId=,
    currentSnapshot='QWAcfc38-9daa-4842-b008-f7fb3dd8439a',
    snapshots=['QWAcfc38-9daa-4842-b008-f7fb3dd8439a'],
    metadata=[AssetMetadata('STRING', 'abcd', 'pqr', 'sds'), AssetMetadata('STRING', 'abcdq', 'pqrq', 'sqds'),
              AssetMetadata('STRING', 'abcddq', 'pqrqd', 'sqdds')]
)

# res = TorchClient.createAsset(asset)
# print(res)

snapshotdata = SnapshotData(
    uuid='WYScfc38-9daa-4842-b008-f7fb3dd8439a',
    associatedItemType=AssociatedItemType.ASSEMBLY,
    associatedItemId=18
)

# res = TorchClient.initialiseSnapshot(snapshotdata)
# print(res)

# resGetAssVersion = TorchClient.getCurrentSnapshot(20)
# print(resGetAssVersion)

assetRelation = CreateAssetRelation(
    fromAssetUUID='feature-bag-assembly.feature_set_1.feature_24',
    assemblyId=20,
    toAssetUUID='feature__uid_21',
    relationType=RelationType.SIBLING,
    currentSnapshot='QWAcfc38-9daa-4842-b008-f7fb3dd8439a',
    snapshots=['QWAcfc38-9daa-4842-b008-f7fb3dd8439a']
)

# assetRelRes = TorchClient.createAssetRelation(assetRelation)
# print(assetRelRes)


createSpan = Span(
    uid='span_run_uid_5',
    pipelineRunId=3
)
# createSpanRes = TorchClient.createSpan(createSpan)
# print(createSpanRes)

spanDict = {
    'span': {
        'finishedAt': None,
        'id': 2,
        'parentSpanId': None,
        'pipelineRunId': 1,
        'startedAt': None,
        'status': 'INITIALIZED',
        'uid': 'span_run_uid_2'
    }
}
spanObj = Span(**spanDict['span'])
# print('spanObj: ', spanObj)
createSpanContext = SpanContext(
    client=TorchClient,
    span=spanObj
)
# print('createSpanContext: ', createSpanContext)
# print(createSpanContext.hasChildren())
# print(createSpanContext.isRoot())
# print('res final : ', createSpanContext.start({'k1': 'v1'}))
# print('res final : ', createSpanContext.end())
# print('res final : ', createSpanContext.sendLogs({'k1':'v1'}, 'logged data..') )
# print('res final : ', createSpanContext.abort({'k3':'3v'}))


createSpanEvent = CreateSpanEvent(
    eventType='SPAN_START',
    contextData={'k1': 'v1'},
    # logData='logged data',
    spanId=2
)
# createSpanEventRes = TorchClient.createSpanEvent(createSpanEvent)
# print(createSpanEventRes)

# assetTypes = TorchClient.getAllAssetType()
# print(assetTypes)

# sourceType = TorchClient.getAllSourceType()
# print(sourceType)

# getAsset = TorchClient.getAssetById(9893)
# getAsset2 = TorchClient.getAssetByUid('postgres-assembly-5450.ad_catalog.ad_catalog.flyway_schema_history')
# print(getAsset2)
# print('get: ', getAsset)

# jobres_  = {
# 'node': {'assetId': None, 'context': {'key21':'value21'} , 'description': 'Generates the monthly sales aggregate tables for the complete year', 'id': 66, 'meta': {'codeLocation': 'https://github.com/acme/reporting/reporting.scala', 'owner': 'vaishvik', 'team': 'backend'}, 'name': 'Monthly Sales Aggregate-20', 'pipelineId': 23, 'type': 'FUNCTIONAL',
#  'uid': 'monthly_sales_aggregate-20'}
#  }

# out = JobResponse(**jobres_['node'])
# # print(out.__dict__)
# print('meta : ',out.uid)

# assetrelationres = {'data': {'currentSnapshot': 'QWAcfc38-9daa-4842-b008-f7fb3dd8439a', 'fromAssetId': 15369, 'id': 208, 'isDeleted': False, 'metadata': None, 'relation': 'SIBLING', 'snapshots': ['QWAcfc38-9daa-4842-b008-f7fb3dd8439a'], 'toAssetId': 15370}}
# print('assetRel ',assetrelationres['data'])
# retRes = AssetRelation(**assetrelationres['data'])
# print('ans-- ', retRes)

# dsRes =  {'data': {'assemblyProperties': None, 'configuration': {'schedule': {'cron': None, 'enabled': False}}, 'conn': None, 'connectionId': None, 'crawler': {'name': 'feature_bag'}, 'createdAt': '2021-04-14T17:43:00.243+05:30', 'currentSnapshot': None, 'description': 'feature bag assembly creation using python sdk', 'id': 23, 'isSecured': False, 'isVirtual': True, 'name': 'Feature_bag_datasource_new_3', 'schedule': None, 'securityConfig': None, 'sourceType': {'connectionTypeId': None, 'id': 21, 'name': 'FEATURE_BAG', 'sourceModel': {'id': 6, 'name': 'ML'}}, 'updatedAt': '2021-04-14T17:43:00.243+05:30'}}
# dsRes_ = DataSource(**dsRes['data'])
# print(dsRes_.sourceType.name)

# pipelineres = {'pipeline':
# 			{
# 			'context': {'context': {}},
# 			 'createdAt': '2021-04-12T13:44:09.229+05:30',
# 			 'currentSnapshot': 'c8308ae5-1816-40df-9e2d-6fd42ce96deb',
# 			 'description': 'Pipeline to create monthly reporting tables',
# 			 'enabled': True,
# 			  'id': 23,
# 			  'interrupt': False,
# 			  'meta': {'codeLocation': '...', 'owner': 'vaishvik', 'team': 'torch'},
# 			  'name': 'Monthly reporting Pipeline-20',
# 			  'notificationChannels': None,
# 			  'schedule': None,
# 			  'scheduled': False,
# 			  'schedulerType': 'INTERNAL',
# 			  'snapshots': ['c8308ae5-1816-40df-9e2d-6fd42ce96deb'],
# 			  'uid': 'monthly_reporting-20',
# 			   'updatedAt': '2021-04-12T13:44:09.229+05:30'
# 		   }
#    }

# pipelineres_ = PipelineResponse(**pipelineres['pipeline'])
# print(pipelineres_)

# assetDict =  {'data': [{'alias': None, 'assembly': {'assemblyProperties': None, 'configuration': None, 'conn': None, 'connectionId': 14, 'crawler': {'name': 'postgresql'}, 'createdAt': '2021-03-05T12:55:33.273+05:30', 'currentSnapshot': '82e5fa30-9a4e-41bc-841c-c4ea2a1efca9', 'description': '', 'id': 9, 'isSecured': False, 'isVirtual': False, 'name': 'postgres-assembly-5450', 'schedule': None, 'securityConfig': None, 'sourceType': {'connectionTypeId': 12, 'id': 10, 'name': 'POSTGRESQL', 'sourceModel': None}, 'updatedAt': '2021-03-16T14:09:45.446+05:30'}, 'assetType': {'canProfile': True, 'canSample': True, 'id': 2, 'name': 'TABLE'}, 'createdAt': '2021-03-05T12:58:28.771+05:30', 'currentSnapshot': '82e5fa30-9a4e-41bc-841c-c4ea2a1efca9', 'description': 'NA', 'id': 9893, 'isCustom': False, 'isDeleted': False, 'name': 'flyway_schema_history', 'parentId': 9892, 'snapshots': ['82e5fa30-9a4e-41bc-841c-c4ea2a1efca9', 'c76b7bc3-dd85-4d3c-b4f3-b6c038aa6505', '99dc62d0-d95c-4156-a398-2c1cc721b192', '9bb37d26-dec6-403a-9a1e-1ccb668b9df9', 'f5060f07-8534-4374-a32a-1908c644984b', '18e892f0-a726-433c-8d38-12bce3f07a39', '3c81ef52-b3eb-4881-be61-476d3b44276e', '3c81ef52-b3eb-4881-be61-476d3b44276e', 'bc80bde9-88cc-4d8e-bdb8-9dde35f08a4f', '17c2996c-1021-4cee-bde5-f3b35543cd6d', '6bfdc24f-d388-4786-b743-2ed955aaa858'], 'sourceType': {'connectionTypeId': 12, 'id': 10, 'name': 'POSTGRESQL', 'sourceModel': None}, 'uid': 'postgres-assembly-5450.ad_catalog.ad_catalog.flyway_schema_history', 'updatedAt': '2021-03-16T14:08:06.346+05:30'}]}
# assetDictRes = TorchClient.convertDictToAsset(assetDict)
# print('ans:: ', assetDictRes)
# import json
# json_object = json.dumps(assetDict, indent = 4)
# print(json_object)
