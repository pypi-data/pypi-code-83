
from pythonapm import constants
from pythonapm.instrumentation.wrapper import wsgi_wrapper

module_info = {
    'flask' : [
        {
            constants.class_str : 'Flask',
            constants.method_str : 'wsgi_app',
            constants.wrapper_str : wsgi_wrapper,
        },
        {
            constants.class_str : 'Flask',
            constants.method_str : 'add_url_rule',
            constants.wrap_args : 3
        }
    ]
}


