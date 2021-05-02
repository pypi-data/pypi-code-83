from localstack.utils.aws import aws_models
ciYjC=super
ciYjn=None
ciYjy=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  ciYjC(LambdaLayer,self).__init__(arn)
  self.cwd=ciYjn
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.ciYjy.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,ciYjy,env=ciYjn):
  ciYjC(RDSDatabase,self).__init__(ciYjy,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,ciYjy,env=ciYjn):
  ciYjC(RDSCluster,self).__init__(ciYjy,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,ciYjy,env=ciYjn):
  ciYjC(AppSyncAPI,self).__init__(ciYjy,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,ciYjy,env=ciYjn):
  ciYjC(AmplifyApp,self).__init__(ciYjy,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,ciYjy,env=ciYjn):
  ciYjC(ElastiCacheCluster,self).__init__(ciYjy,env=env)
class TransferServer(BaseComponent):
 def __init__(self,ciYjy,env=ciYjn):
  ciYjC(TransferServer,self).__init__(ciYjy,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,ciYjy,env=ciYjn):
  ciYjC(CloudFrontDistribution,self).__init__(ciYjy,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,ciYjy,env=ciYjn):
  ciYjC(CodeCommitRepository,self).__init__(ciYjy,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
