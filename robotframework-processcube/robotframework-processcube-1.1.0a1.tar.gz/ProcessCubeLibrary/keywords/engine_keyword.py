
class EngineKeyword:

    def __init__(self, client, **kwargs):
        self._client = client

    def get_engine_info(self):
        info = self._client.info()

        return info
