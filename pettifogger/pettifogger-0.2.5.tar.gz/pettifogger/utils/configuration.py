class GlobalConfiguration:
    def __init__(self):
        self.suppress_suspicions = False
        self.no_fail_on_error = False
        self.fail_on_suspicions = False

__global_configuration = GlobalConfiguration()

def get_global_configuration():
    global __global_configuration
    return __global_configuration

def set_global_configuration(conf):
    global __global_configuration
    __global_configuration = conf