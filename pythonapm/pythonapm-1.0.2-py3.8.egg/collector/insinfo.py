
import json
import os
from pythonapm.collector.rescodes import get_retry_counter, is_valid_rescode, is_retry_limit_exceeded
from pythonapm.util import current_milli_time, is_non_empty_string, is_empty_string
from pythonapm.constants import manage_agent
from pythonapm.logger import agentlogger

class Instanceinfo:

    def __init__(self):
        self.last_reported = None
        self.retry_counter = 1
        self.status = manage_agent
        self.modified_time = current_milli_time()

    def update_instance_info(self, rescode):
        self.update_last_reported()
        if self.status is not rescode:
            self.status = rescode if rescode is not None else manage_agent
            self.retry_counter = 1

    def update_status(self, rescode):
        self.update_last_reported()
        if is_valid_rescode(rescode) is not True:
            return

        self.retry_counter = self.retry_counter+1 if self.status == rescode else 1
        if self.retry_counter==1:
            self.status = rescode
            return

        if is_retry_limit_exceeded(rescode, self.retry_counter):
            agentlogger.critical(' Retry limit exceeded for response code :'+ 
                            str(rescode) +' so Agent goes to shutdown state')
            self.status = 0

    def get_status(self):
        return self.status

    def update_last_reported(self):
        self.last_reported = current_milli_time()

    def get_modiefied_time(self):
        return self.modified_time

    def get_retry_counter(self):
        return self.retry_counter

    def get_last_reported(self):
        return self.last_reported
    


