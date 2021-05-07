from localstack.utils.aws import aws_models
ztSwc=super
ztSwl=None
ztSwB=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  ztSwc(LambdaLayer,self).__init__(arn)
  self.cwd=ztSwl
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.ztSwB.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,ztSwB,env=ztSwl):
  ztSwc(RDSDatabase,self).__init__(ztSwB,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,ztSwB,env=ztSwl):
  ztSwc(RDSCluster,self).__init__(ztSwB,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,ztSwB,env=ztSwl):
  ztSwc(AppSyncAPI,self).__init__(ztSwB,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,ztSwB,env=ztSwl):
  ztSwc(AmplifyApp,self).__init__(ztSwB,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,ztSwB,env=ztSwl):
  ztSwc(ElastiCacheCluster,self).__init__(ztSwB,env=env)
class TransferServer(BaseComponent):
 def __init__(self,ztSwB,env=ztSwl):
  ztSwc(TransferServer,self).__init__(ztSwB,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,ztSwB,env=ztSwl):
  ztSwc(CloudFrontDistribution,self).__init__(ztSwB,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,ztSwB,env=ztSwl):
  ztSwc(CodeCommitRepository,self).__init__(ztSwB,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
