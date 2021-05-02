from localstack.utils.aws import aws_models
AYqRT=super
AYqRd=None
AYqRB=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  AYqRT(LambdaLayer,self).__init__(arn)
  self.cwd=AYqRd
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.AYqRB.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,AYqRB,env=AYqRd):
  AYqRT(RDSDatabase,self).__init__(AYqRB,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,AYqRB,env=AYqRd):
  AYqRT(RDSCluster,self).__init__(AYqRB,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,AYqRB,env=AYqRd):
  AYqRT(AppSyncAPI,self).__init__(AYqRB,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,AYqRB,env=AYqRd):
  AYqRT(AmplifyApp,self).__init__(AYqRB,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,AYqRB,env=AYqRd):
  AYqRT(ElastiCacheCluster,self).__init__(AYqRB,env=env)
class TransferServer(BaseComponent):
 def __init__(self,AYqRB,env=AYqRd):
  AYqRT(TransferServer,self).__init__(AYqRB,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,AYqRB,env=AYqRd):
  AYqRT(CloudFrontDistribution,self).__init__(AYqRB,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,AYqRB,env=AYqRd):
  AYqRT(CodeCommitRepository,self).__init__(AYqRB,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
