
from pythonapm import constants
from pythonapm.instrumentation.wrapper import wsgi_wrapper

module_info = {
    'django.core.handlers.wsgi' : [
        {
            constants.class_str : 'WSGIHandler',
            constants.method_str : '__call__',
            constants.wrapper_str : wsgi_wrapper,
        }
    ],
    'django.conf.urls' : [
        {
            constants.method_str : 'url',
            constants.wrap_args : 1,
        }
    ],
    'django.urls' : [
        {
            constants.method_str : 'path',
            constants.wrap_args : 1,
        }
    ],
    'django.template' : [
        {
            constants.class_str : 'Template',
            constants.method_str : 'render',
        }
    ]
}