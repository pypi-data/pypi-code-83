
from importlib import import_module
from pythonapm.instrumentation import instrument_method
from pythonapm.logger import agentlogger
from pythonapm import constants

methods = [
    'process_request', 
    'process_view', 
    'process_exception', 
    'process_template_response', 
    'process_response'
]

def instrument_middlewares():
    try:
        from django.conf import settings
        middleware = getattr(settings, "MIDDLEWARE", None) or \
            getattr(settings, "MIDDLEWARE_CLASSES", None)
        
        if middleware is None:
            return 

        for each in middleware:
            module_path, class_name = each.rsplit('.', 1)
            act_module = import_module(module_path)
            for each_method in methods:
                method_info = {
                    constants.class_str : class_name,
                    constants.method_str : each_method,
                }
                instrument_method(module_path, act_module, method_info)


    except Exception as exc:
        agentlogger('django middleware instrumentation error', exc)


