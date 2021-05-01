
import requests
import json
from pythonapm.logger import agentlogger
from pythonapm.agentfactory import get_agent

def send_req(path_uri, payload):
    response = ''
    response_data = {}
    try:
        config = get_agent().get_config()
        url = config.get_collector_domain() + path_uri
        query_param = 'licenseKey='+ config.get_license_key()+'&projectId='+config.get_project_id()
        complete_url = url + '?' + query_param
        headers = {'content-type': 'application/json'}
        payload_str = json.dumps(payload)
        agentlogger.info('sending request to ' + url)
        if config.is_payload_print_enabled():
            agentlogger.info('payload :'+ payload_str)

        response = requests.post(complete_url, data=payload_str, headers=headers)
        response_data = response.json()
    except Exception:
        agentlogger.exception(path_uri+' req error '+ str(response))

    agentlogger.info('response for '+ path_uri+' request :'+ json.dumps(response_data))
    return response_data