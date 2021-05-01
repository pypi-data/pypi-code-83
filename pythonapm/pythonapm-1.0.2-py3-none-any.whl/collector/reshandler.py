
from pythonapm.logger import agentlogger
from pythonapm.agentfactory import get_agent
from pythonapm import constants
from pythonapm.collector.rescodes import get_rescode_message

def handle_connect_response(res_data={}):
    try:
        if type(res_data) is not dict:
            return False

        data = res_data.get('data', None)

        if data is None or type(data) is not dict:
            return False

        res_code = data.get(constants.rescode, None)
        insinfo = get_agent().get_ins_info()

        if res_code is not None and insinfo.get_status() != res_code:
            agentlogger.critical('received response code :'+ str(res_code))

        insinfo.update_instance_info(res_code)
        return True
    except Exception:
        agentlogger.exception('connect response handler')
        return False


def handle_data_response(res_data={}):
    try:
        if type(res_data) is not dict:
            return False

        data = res_data.get('data', None)

        if data is None:
            return False

        res_code = data.get(constants.rescode, None)
        agent = get_agent()
        instance_info = agent.get_ins_info()

        if res_code is not None and res_code!=instance_info.get_status():
            agentlogger.critical('received response code :'+ get_rescode_message(res_code))
            instance_info.update_status(res_code)

        return True
    except Exception:
        agentlogger.exception('data response handler')
        return False
    



