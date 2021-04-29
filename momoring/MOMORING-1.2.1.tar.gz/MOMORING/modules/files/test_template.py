def get_test_template():
    txt = """\
import os


def prepare():
    # set default path
    os.environ.setdefault('DATAPATH', os.path.join('path', 'datapath'))
    os.environ.setdefault('STASHPATH', os.path.join('path', 'stashpath'))
    os.environ.setdefault('SAVEDPATH', os.path.join('path', 'savedpath'))
    
    # set default env
    json_template = {
        'env': {'None': None},
        'limit': 1
    }
    
    for i in json_template['env'].keys():
        os.environ.setdefault(i, str(json_template['env'][i]))


if __name__ == '__main__':
    prepare()
"""
    return txt
