from localstack.utils.aws import aws_models
xoIps=super
xoIpY=None
xoIpT=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  xoIps(LambdaLayer,self).__init__(arn)
  self.cwd=xoIpY
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.xoIpT.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,xoIpT,env=xoIpY):
  xoIps(RDSDatabase,self).__init__(xoIpT,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,xoIpT,env=xoIpY):
  xoIps(RDSCluster,self).__init__(xoIpT,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,xoIpT,env=xoIpY):
  xoIps(AppSyncAPI,self).__init__(xoIpT,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,xoIpT,env=xoIpY):
  xoIps(AmplifyApp,self).__init__(xoIpT,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,xoIpT,env=xoIpY):
  xoIps(ElastiCacheCluster,self).__init__(xoIpT,env=env)
class TransferServer(BaseComponent):
 def __init__(self,xoIpT,env=xoIpY):
  xoIps(TransferServer,self).__init__(xoIpT,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,xoIpT,env=xoIpY):
  xoIps(CloudFrontDistribution,self).__init__(xoIpT,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,xoIpT,env=xoIpY):
  xoIps(CodeCommitRepository,self).__init__(xoIpT,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
