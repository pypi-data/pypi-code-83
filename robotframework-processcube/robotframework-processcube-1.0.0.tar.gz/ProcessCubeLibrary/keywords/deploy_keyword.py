
class DeployKeyword:

    def __init__(self, client, **kwargs):
        self._client = client

    def deploy_processmodel(self, pathname):
        self._client.process_defintion_deploy_by_pathname(pathname)
