import boto3, json, logging

def removeNone(data):
    return { k:v for k, v in data.items() if v is not None }

class LogFunction:
  def __init__(self, stackName= 'villa-wallet-log-dev-doc', user=None, pw=None, sessionToken=None, region='ap-southeast-1'):
    self.lambdaClient = boto3.client(
        'lambda',
        aws_access_key_id = user,
        aws_secret_access_key = pw ,
        aws_session_token = sessionToken,
        region_name = region
      )
    self.stackName = stackName

  def invoke(self, functionName, data:dict):
    response = self.lambdaClient.invoke(
        FunctionName = functionName,
        InvocationType = 'RequestResponse',
        Payload=json.dumps(data)
    )
    return json.loads(response['Payload'].read())



  def getLog(self, data:dict):
    functionName = f'{self.stackName}-get'
    return self.invoke(functionName = functionName, data=data)

  def setLog(self, data:dict):
    functionName = f'{self.stackName}-create'
    return self.invoke(functionName = functionName, data=data)
