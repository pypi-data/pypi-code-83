from sofacomponents.lib.BaseFactory import BaseFactory


class SofaFactory(BaseFactory):
    def __init__(self, debug=False):
        self._defaults = dict()
        if debug:
            self._defaults.update({"printLog": True})

    def Plugins(self, *names):
        plugins = set(["SofaPython"])
        for x in names:
            plugins.add(x)
        plugins = " ".join(plugins)
        return super().RequiredPlugin(pluginName=plugins)
