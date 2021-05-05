from localstack.utils.aws import aws_models
ICLRn=super
ICLRH=None
ICLRy=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  ICLRn(LambdaLayer,self).__init__(arn)
  self.cwd=ICLRH
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.ICLRy.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,ICLRy,env=ICLRH):
  ICLRn(RDSDatabase,self).__init__(ICLRy,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,ICLRy,env=ICLRH):
  ICLRn(RDSCluster,self).__init__(ICLRy,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,ICLRy,env=ICLRH):
  ICLRn(AppSyncAPI,self).__init__(ICLRy,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,ICLRy,env=ICLRH):
  ICLRn(AmplifyApp,self).__init__(ICLRy,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,ICLRy,env=ICLRH):
  ICLRn(ElastiCacheCluster,self).__init__(ICLRy,env=env)
class TransferServer(BaseComponent):
 def __init__(self,ICLRy,env=ICLRH):
  ICLRn(TransferServer,self).__init__(ICLRy,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,ICLRy,env=ICLRH):
  ICLRn(CloudFrontDistribution,self).__init__(ICLRy,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,ICLRy,env=ICLRH):
  ICLRn(CodeCommitRepository,self).__init__(ICLRy,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
