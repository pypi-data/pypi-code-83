
from pythonapm.util import current_milli_time
from pythonapm.agentfactory import get_agent
from pythonapm.util import is_empty_string, get_normalized_url

class Transaction:

    def __init__(self, wsgi_environ={}, root_tracker_info={}):
        url = wsgi_environ.get('PATH_INFO', '')
        self.url = get_normalized_url(url)
        self.query = wsgi_environ.get('QUERY_STRING', '')
        self.method = wsgi_environ.get('REQUEST_METHOD', '')
        self.start_time = current_milli_time()
        self.end_time = None
        self.rt = 0
        self.completed = False
        self.status_code = None
        self.exceptions_info = {}

    def end_txn(self, res=None, err=None):
        agent = get_agent()
        if agent.is_data_collection_allowed() is False:
            return

        self.end_time = current_milli_time()
        self.check_and_add_error(err)
        
        if res is not None and hasattr(res,'status_code'):
            self.status_code = res.status_code
            
        self.rt = self.end_time-self.start_time
        self.completed = True
        agent.get_metric_store().add_web_txn(self)

    def check_and_add_error(self, err):
        if err is None:
            return

        err_name = 'Error'
        if hasattr(type(err), '__name__'):
            err_name = type(err).__name__

        err_count = self.exceptions_info.get(err_name, 0)
        self.exceptions_info[err_name] = err_count+1

    def get_url(self):
        return self.url

    def get_method(self):
        return self.method

    def get_rt(self):
        return self.rt 

    def get_start_time(self):
        return self.start_time

    def get_query_param(self):
        return self.query

    def get_exceptions_info(self):
        return self.exceptions_info

    def get_status_code(self):
        return self.status_code

    def is_completed(self):
        return self.completed

    def is_error_txn(self):
        if type(self.status_code) is int:
            if self.status_code >= 400:
                return True
        
        return False


    