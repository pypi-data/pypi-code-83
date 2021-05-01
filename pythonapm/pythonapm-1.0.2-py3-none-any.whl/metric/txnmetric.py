
from pythonapm.agentfactory import get_agent

class TxnMetric:

    def __init__(self):
        self.url = ''
        self.method = ''
        self.rt = 0
        self.min_rt = 0 
        self.max_rt = 0
        self.err_rt = 0
        self.count = 0
        self.err_count = 0
        self.error_codes = {}
        self.exceptions_info = {}

    def update_req_count(self, txn):
        if txn.is_error_txn():
            self.err_count += 1
        else:
            self.count += 1


    def aggregate(self, txn):
        self.url = txn.get_url()
        self.method = txn.get_method()
        if txn.is_error_txn():
            self.err_count += 1
            self.err_rt += txn.get_rt()
            self.aggregate_txn_sub_resources(txn)
            return

        self.aggregate_non_error_txn(txn)

    def aggregate_non_error_txn(self, txn):
        self.rt += txn.get_rt()
        self.count += 1
        self.aggregate_txn_sub_resources(txn)
        if self.min_rt==0 or self.min_rt>txn.get_rt():
            self.min_rt = txn.get_rt()

        if self.max_rt==0 or self.max_rt<txn.get_rt():
            self.max_rt = txn.get_rt()


    def aggregate_txn_sub_resources(self, txn):
        self.aggregate_errorcode(txn)
        self.aggregate_exceptions(txn.get_exceptions_info())
    
    def aggregate_exceptions(self, cur_exc_info={}):
        if len(cur_exc_info)<=0:
            return

        exc_info = self.exceptions_info.keys()
        for each_error in cur_exc_info.keys():
            if each_error in exc_info:
                self.exceptions_info[each_error] += cur_exc_info[each_error]
            else:
                self.exceptions_info[each_error] = cur_exc_info[each_error]

    def aggregate_errorcode(self, txn):
        if txn.is_error_txn() and txn.get_status_code()>=400:
            if txn.get_status_code() in self.error_codes:
                self.error_codes[txn.get_status_code()] += 1
            else:
                self.error_codes[txn.get_status_code()] = 1


    def get_formatted_data(self):
        return {
            'url': self.url,
            'method': self.method,
            'rt': self.rt,
            'minrt': self.min_rt,
            'maxrt': self.max_rt,
            'errorrt': self.err_rt,
            'count': self.count,
            'errcount': self.err_count,
            'errors': self.error_codes,
            'exceptions': self.exceptions_info,
        }

    def get_count(self):
        return self.count

    def get_error_count(self):
        return self.err_count

    def get_rt(self):
        return self.rt

    def get_error_rt(self):
        return self.err_rt

    def get_min_rt(self):
        return self.min_rt

    def get_max_rt(self):
        return self.max_rt

    def get_exceptions_info(self):
        return self.exceptions_info
