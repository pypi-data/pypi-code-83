from localstack.utils.aws import aws_models
GBjzn=super
GBjza=None
GBjzP=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  GBjzn(LambdaLayer,self).__init__(arn)
  self.cwd=GBjza
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.GBjzP.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,GBjzP,env=GBjza):
  GBjzn(RDSDatabase,self).__init__(GBjzP,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,GBjzP,env=GBjza):
  GBjzn(RDSCluster,self).__init__(GBjzP,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,GBjzP,env=GBjza):
  GBjzn(AppSyncAPI,self).__init__(GBjzP,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,GBjzP,env=GBjza):
  GBjzn(AmplifyApp,self).__init__(GBjzP,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,GBjzP,env=GBjza):
  GBjzn(ElastiCacheCluster,self).__init__(GBjzP,env=env)
class TransferServer(BaseComponent):
 def __init__(self,GBjzP,env=GBjza):
  GBjzn(TransferServer,self).__init__(GBjzP,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,GBjzP,env=GBjza):
  GBjzn(CloudFrontDistribution,self).__init__(GBjzP,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,GBjzP,env=GBjza):
  GBjzn(CodeCommitRepository,self).__init__(GBjzP,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
