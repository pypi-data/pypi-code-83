
import os
import pythonapm
import pythonapm.constants as constants
from pythonapm.logger import agentlogger
from pythonapm.util import is_empty_string, is_non_empty_string

class Configuration:

    def __init__(self):
        self.license_key = os.getenv(constants.license_key_env, '')
        self.project_id = os.getenv(constants.project_key_env, '')
        self.collector_domain = get_collector_domain()
        self.agent_version = pythonapm.version
        payload_config = os.getenv(constants.agent_print_payload, '')
        self.print_payload = False if is_empty_string(payload_config) else True
        self.installed_path = pythonapm.installed_path

    def is_configured_properly(self):
        if is_empty_string(self.license_key):
            return False

        if is_empty_string(self.project_id):
            return False

        return True
            
    def get_license_key(self):
        return self.license_key

    def get_project_id(self):
        return self.project_id

    def get_collector_domain(self):
        return self.collector_domain

    def get_agent_version(self):
        return self.agent_version

    def get_installed_dir(self):
        return self.installed_path

    def is_payload_print_enabled(self):
        return self.print_payload
    

def get_collector_domain():
    domain = os.getenv(constants.agent_collector_host, '')
    if is_non_empty_string(domain):
        return domain
    
    return constants.collector_domain

