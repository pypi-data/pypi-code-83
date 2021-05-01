
from pythonapm.agentfactory import get_agent
from pythonapm.logger import agentlogger
from pythonapm.metric.txnmetric import TxnMetric
from pythonapm.util import is_empty_string

class Metricstore:

    def __init__(self):
        self.web_txn_metric={}

    def add_web_txn(self, txn):
        try:
            if(txn.is_completed() is not True):
                return False

            txnname = txn.get_method() + ' - ' + txn.get_url()
            match = txnname in self.web_txn_metric  
        
            if match is not True:
                metric = TxnMetric()
                metric.aggregate(txn)
                self.web_txn_metric[txnname] = metric
                return True

            if len(self.web_txn_metric) <= 100:
                matched_txn = self.web_txn_metric.get(txnname)
                matched_txn.aggregate(txn)
                self.web_txn_metric[txnname] = matched_txn

            return True

        except Exception:
            agentlogger.exception('unable to add web txn')

        return False
               

    def get_formatted_data(self):
        formatted_data = []

        for txn_name in self.web_txn_metric.keys():
            txnmetric = self.web_txn_metric[txn_name]
            txn_data = txnmetric.get_formatted_data()
            formatted_data.append(txn_data)            

        return formatted_data

    def cleanup(self):
        self.web_txn_metric={}
    
    def get_webtxn_metric(self):
        return self.web_txn_metric


