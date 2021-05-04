from localstack.utils.aws import aws_models
RIpFl=super
RIpFS=None
RIpFN=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  RIpFl(LambdaLayer,self).__init__(arn)
  self.cwd=RIpFS
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.RIpFN.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,RIpFN,env=RIpFS):
  RIpFl(RDSDatabase,self).__init__(RIpFN,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,RIpFN,env=RIpFS):
  RIpFl(RDSCluster,self).__init__(RIpFN,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,RIpFN,env=RIpFS):
  RIpFl(AppSyncAPI,self).__init__(RIpFN,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,RIpFN,env=RIpFS):
  RIpFl(AmplifyApp,self).__init__(RIpFN,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,RIpFN,env=RIpFS):
  RIpFl(ElastiCacheCluster,self).__init__(RIpFN,env=env)
class TransferServer(BaseComponent):
 def __init__(self,RIpFN,env=RIpFS):
  RIpFl(TransferServer,self).__init__(RIpFN,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,RIpFN,env=RIpFS):
  RIpFl(CloudFrontDistribution,self).__init__(RIpFN,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,RIpFN,env=RIpFS):
  RIpFl(CodeCommitRepository,self).__init__(RIpFN,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
