from localstack.utils.aws import aws_models
CLNgf=super
CLNgw=None
CLNgJ=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  CLNgf(LambdaLayer,self).__init__(arn)
  self.cwd=CLNgw
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.CLNgJ.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,CLNgJ,env=CLNgw):
  CLNgf(RDSDatabase,self).__init__(CLNgJ,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,CLNgJ,env=CLNgw):
  CLNgf(RDSCluster,self).__init__(CLNgJ,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,CLNgJ,env=CLNgw):
  CLNgf(AppSyncAPI,self).__init__(CLNgJ,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,CLNgJ,env=CLNgw):
  CLNgf(AmplifyApp,self).__init__(CLNgJ,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,CLNgJ,env=CLNgw):
  CLNgf(ElastiCacheCluster,self).__init__(CLNgJ,env=env)
class TransferServer(BaseComponent):
 def __init__(self,CLNgJ,env=CLNgw):
  CLNgf(TransferServer,self).__init__(CLNgJ,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,CLNgJ,env=CLNgw):
  CLNgf(CloudFrontDistribution,self).__init__(CLNgJ,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,CLNgJ,env=CLNgw):
  CLNgf(CodeCommitRepository,self).__init__(CLNgJ,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
