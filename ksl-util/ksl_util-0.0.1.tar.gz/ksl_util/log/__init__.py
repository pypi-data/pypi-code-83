from ksl_util.time.time_check import current_time
import inspect, re

def printlog(*args, **kwargs):
    time = current_time()
    end = '\n'
    method_name = ''

    if kwargs.__contains__('end'):
        end = kwargs['end']

    if kwargs.__contains__('method') and kwargs['method'] == True:
        print('{:<30} :'.format(time), *args)
        print('{:<30} :'.format(inspect.stack()[1][2]), inspect.stack()[1][3], end=end)
        # print(inspect.stack())
        return

    if 'save_txt' in kwargs:
        file = kwargs['save_txt']
        txt = '{:<30} :'.format(time)
        for arg in args:
            txt += arg
        txt += end
        file.write('%s' % txt)

    print('{:<30} :'.format(time), *args, end=end)


def printcommand(command, *args, **kwargs):
    
    printlog('{:<15}'.format('(%s)' % command), *args)


def class_check(_object, _class):

    assert _class.__name__ == _object.__class__.__name__ or _class.__name__ in [name.__name__ for name in _object.__class__.__bases__], 'object of <%s> is not a class of <%s>' % (_object.__class__.__name__, _class.__name__)


def print_varname(var_name):
    print('{:<30}'.format(var_name), eval(var_name))

