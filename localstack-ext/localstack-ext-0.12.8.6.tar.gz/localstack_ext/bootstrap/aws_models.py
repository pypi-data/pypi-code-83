from localstack.utils.aws import aws_models
qBvGc=super
qBvGx=None
qBvGL=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  qBvGc(LambdaLayer,self).__init__(arn)
  self.cwd=qBvGx
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.qBvGL.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,qBvGL,env=qBvGx):
  qBvGc(RDSDatabase,self).__init__(qBvGL,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,qBvGL,env=qBvGx):
  qBvGc(RDSCluster,self).__init__(qBvGL,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,qBvGL,env=qBvGx):
  qBvGc(AppSyncAPI,self).__init__(qBvGL,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,qBvGL,env=qBvGx):
  qBvGc(AmplifyApp,self).__init__(qBvGL,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,qBvGL,env=qBvGx):
  qBvGc(ElastiCacheCluster,self).__init__(qBvGL,env=env)
class TransferServer(BaseComponent):
 def __init__(self,qBvGL,env=qBvGx):
  qBvGc(TransferServer,self).__init__(qBvGL,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,qBvGL,env=qBvGx):
  qBvGc(CloudFrontDistribution,self).__init__(qBvGL,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,qBvGL,env=qBvGx):
  qBvGc(CodeCommitRepository,self).__init__(qBvGL,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
