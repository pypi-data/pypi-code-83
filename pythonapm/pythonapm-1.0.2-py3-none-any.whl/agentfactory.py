
from pythonapm.logger import agentlogger


agent_instance = None

def get_agent():
    global agent_instance
    
    if agent_instance is None:
        try:
            from pythonapm.agent import initalize
            agent_instance = initalize()
            agentlogger.info('agent initialized')
        except Exception:
            agentlogger.exception('agent initialization')
    
    return agent_instance