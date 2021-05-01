
from pythonapm.agentfactory import get_agent
from pythonapm.logger import agentlogger
from pythonapm.constants import wrap_args
from pythonapm.util import is_callable
from pythonapm.context import clear_cur_context
from pythonapm.constants import component_str, extract_info
from pythonapm.context import is_no_active_txn


def wsgi_wrapper(original, module, method_info):
    def wrapper(*args, **kwargs):
        cur_txn = None 
        res = None
        agent = get_agent()
        try:
            wsgi_environ = args[1]
            cur_txn = agent.check_and_create_txn(wsgi_environ)
            res = original(*args, **kwargs)
            agent.end_txn(cur_txn, res)
        except Exception as exc:
            agent.end_txn(cur_txn, err=exc)
            raise exc
        finally:
            clear_cur_context()
                 
        return res

    return wrapper


def default_wrapper(original, module, method_info):
    def wrapper(*args, **kwargs):
        if is_no_active_txn():
            return original(*args, **kwargs)
       
        res = None 
        agent = get_agent()
        try:
            res = original(*args, **kwargs)
        except Exception as exc:
            agent.track_exception(exc)
            raise exc

        return res

    # special handling for flask route decorator
    wrapper.__name__ = original.__name__
    return wrapper

def copy_attributes(source, dest):
    try:
        for att in source.__dict__:
            setattr(dest, att, getattr(source, att))
        
    except Exception:
        agentlogger.exception('copying attribute')



def args_wrapper(original, module, method_info):
    def wrapper(*args, **kwargs): 
        if wrap_args in method_info:
            args_index = method_info[wrap_args]
            if isinstance(args, (list, tuple)) and len(args)> args_index:
                if is_callable(args[args_index]):
                    try:
                        act_method = args[args_index]
                        temp = list(args)
                        module_name = act_method.__module__
                        args_method_info = { 'method' : act_method.__name__ }
                        new_method = default_wrapper(act_method, module_name, args_method_info)
                        copy_attributes(act_method, new_method)
                        temp[args_index] = new_method
                        args = temp
                    except Exception:
                        agentlogger.exception('error in args wrapper')

        
        return original(*args, **kwargs)
    
    return wrapper




