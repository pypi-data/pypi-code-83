from localstack.utils.aws import aws_models
ENYlB=super
ENYlP=None
ENYlF=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  ENYlB(LambdaLayer,self).__init__(arn)
  self.cwd=ENYlP
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.ENYlF.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,ENYlF,env=ENYlP):
  ENYlB(RDSDatabase,self).__init__(ENYlF,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,ENYlF,env=ENYlP):
  ENYlB(RDSCluster,self).__init__(ENYlF,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,ENYlF,env=ENYlP):
  ENYlB(AppSyncAPI,self).__init__(ENYlF,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,ENYlF,env=ENYlP):
  ENYlB(AmplifyApp,self).__init__(ENYlF,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,ENYlF,env=ENYlP):
  ENYlB(ElastiCacheCluster,self).__init__(ENYlF,env=env)
class TransferServer(BaseComponent):
 def __init__(self,ENYlF,env=ENYlP):
  ENYlB(TransferServer,self).__init__(ENYlF,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,ENYlF,env=ENYlP):
  ENYlB(CloudFrontDistribution,self).__init__(ENYlF,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,ENYlF,env=ENYlP):
  ENYlB(CodeCommitRepository,self).__init__(ENYlF,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
