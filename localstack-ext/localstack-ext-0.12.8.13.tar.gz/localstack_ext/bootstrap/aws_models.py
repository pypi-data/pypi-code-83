from localstack.utils.aws import aws_models
WngCS=super
WngCz=None
WngCp=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  WngCS(LambdaLayer,self).__init__(arn)
  self.cwd=WngCz
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.WngCp.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,WngCp,env=WngCz):
  WngCS(RDSDatabase,self).__init__(WngCp,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,WngCp,env=WngCz):
  WngCS(RDSCluster,self).__init__(WngCp,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,WngCp,env=WngCz):
  WngCS(AppSyncAPI,self).__init__(WngCp,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,WngCp,env=WngCz):
  WngCS(AmplifyApp,self).__init__(WngCp,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,WngCp,env=WngCz):
  WngCS(ElastiCacheCluster,self).__init__(WngCp,env=env)
class TransferServer(BaseComponent):
 def __init__(self,WngCp,env=WngCz):
  WngCS(TransferServer,self).__init__(WngCp,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,WngCp,env=WngCz):
  WngCS(CloudFrontDistribution,self).__init__(WngCp,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,WngCp,env=WngCz):
  WngCS(CodeCommitRepository,self).__init__(WngCp,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
