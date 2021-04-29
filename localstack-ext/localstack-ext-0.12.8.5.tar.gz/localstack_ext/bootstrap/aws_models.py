from localstack.utils.aws import aws_models
fybTe=super
fybTr=None
fybTH=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  fybTe(LambdaLayer,self).__init__(arn)
  self.cwd=fybTr
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.fybTH.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,fybTH,env=fybTr):
  fybTe(RDSDatabase,self).__init__(fybTH,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,fybTH,env=fybTr):
  fybTe(RDSCluster,self).__init__(fybTH,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,fybTH,env=fybTr):
  fybTe(AppSyncAPI,self).__init__(fybTH,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,fybTH,env=fybTr):
  fybTe(AmplifyApp,self).__init__(fybTH,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,fybTH,env=fybTr):
  fybTe(ElastiCacheCluster,self).__init__(fybTH,env=env)
class TransferServer(BaseComponent):
 def __init__(self,fybTH,env=fybTr):
  fybTe(TransferServer,self).__init__(fybTH,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,fybTH,env=fybTr):
  fybTe(CloudFrontDistribution,self).__init__(fybTH,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,fybTH,env=fybTr):
  fybTe(CodeCommitRepository,self).__init__(fybTH,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
