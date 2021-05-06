__all__ = [
    'connect',
    'orchestrate',
    'sign_up'
]

def connect(api_key):
    from pyrasgo.rasgo import Rasgo
    return Rasgo(api_key=api_key)

def orchestrate(api_key):
    from pyrasgo.orchestration import RasgoOrchestration
    return RasgoOrchestration(api_key=api_key)

def sign_up():
    import webbrowser
    webbrowser.open("https://app.rasgoml.com/account/register?pyrasgo=true")