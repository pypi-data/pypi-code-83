from . import woodpecker_pb2_grpc as importStub

class WoodpeckerService(object):

    def __init__(self, router):
        self.connector = router.get_connection(WoodpeckerService, importStub.WoodpeckerStub)

    def start(self, request, timeout=None):
        return self.connector.create_request('start', request, timeout)

    def schedule(self, request, timeout=None):
        return self.connector.create_request('schedule', request, timeout)

    def stop(self, request, timeout=None):
        return self.connector.create_request('stop', request, timeout)