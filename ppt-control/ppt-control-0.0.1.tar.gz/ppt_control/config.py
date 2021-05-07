from configparser import ConfigParser
from pkg_resources import Requirement, resource_filename

global prefs
prefs = None

defaults = {
        'Main': {
            'logging': 'info',
            'cache': r'''C:\Windows\Temp\ppt-cache''',
            'cache_format': 'JPG',
            'cache_timeout': 5*60,
            'blackwhite': 'both'
        },
        'HTTP': {
            'interface': '',
            'port': 80
        },
        'WebSocket': {
            'interface': '0.0.0.0',
            'port': 5678
        }
}


def loadconf(configpaths):
    """
    Initial setup for a ConfigParser object. `configpaths` should be a list of
    configuration files to load (typically only one). To use the generated
    ConfigParser, use `import logparse.config` and then `config.prefs.get(..)`.
    The prefs object is returned after creation as a convenience but this method
    should only be called once per runtime.
    """
    prefs = ConfigParser()
    prefs.read_dict(defaults)
    try:
        success = prefs.read(configpaths)
        print("Loaded {0} config file(s): {1}".format(
                str(len(success)), str(success)))
    except Exception as e:
        print("Error processing config: " + str(e))
    return prefs

