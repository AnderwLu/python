class PluginMeta(type):
    registry = {}
    def __new__(cls, name, bases, namespace, /, **kwds):
        #  cls PluginMeta name Plugin
        return super().__new__(cls,name, bases, namespace, **kwds)
    def __init__(self, name, bases, dict, /, **kwds):
        if name != "Plugin":
            self.registry[name] = self
        super().__init__(name, bases, dict, **kwds)

class Plugin(metaclass=PluginMeta):
    pass

class ImagePlugin(Plugin):
    pass

class TextPlugin(Plugin):
    pass

print(PluginMeta.registry)
# 应该输出类似：{'ImagePlugin': <class '__main__.ImagePlugin'>, 'TextPlugin': <class '__main__.TextPlugin'>}
