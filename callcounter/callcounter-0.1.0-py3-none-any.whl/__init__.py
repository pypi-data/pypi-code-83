__version__ = '0.1.0'
project_token = None
debug = False
track = lambda request: request.get_host().startswith('api.') or request.path.startswith('/api')
