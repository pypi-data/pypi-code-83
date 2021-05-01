
import json
from pythonapm.agentfactory import get_agent
from pythonapm.logger import agentlogger
from pythonapm import constants
from pythonapm.util import current_milli_time
from pythonapm.collector.reqhandler import send_req
from pythonapm.collector.rescodes import is_allowed_to_send_request, get_rescode_message
from pythonapm.collector.reshandler import handle_data_response

def get_data_with_time(data):
    return {
        'info': {
            'time': current_milli_time()
        },
        'data': data
    }

def process_collected_data():
    ins_info = get_agent().get_ins_info()
    status = ins_info.get_status()
    metric_store = get_agent().get_metric_store()
    agentlogger.debug('[process_collected_data] ' + get_rescode_message(status))
    
    if status == constants.manage_agent:
        txn_data = metric_store.get_formatted_data()
        agentlogger.info('sending metrics of size ' + str(len(txn_data)))
        data_response = send_req(constants.api_data, get_data_with_time(txn_data))
        handle_data_response(data_response)

    elif status == constants.unmanage_agent:
        trace_response = send_req(constants.api_data, get_data_with_time([]))
        handle_data_response(trace_response)

    else:
        if is_allowed_to_send_request(ins_info.get_status(), ins_info.get_retry_counter()):
            payload = get_data_with_time([])
            response = send_req(constants.api_data, payload)
            handle_data_response(response)



