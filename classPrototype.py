import copy


class Title(object):
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, attrs):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        return obj


class Text(object):
    """1111"""


prototype = Title()
prototype.register('bird', Text())

owl = prototype.clone('bird', {'name': 'Owl'})
print(type(owl), owl.name)  # <class '__main__.Bird'> Owl

duck = prototype.clone('bird', {'name': 'Duck'})
print(type(duck), duck.name)  # <class '__main__.Bird'> Duck