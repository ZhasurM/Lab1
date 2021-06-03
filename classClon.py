from classPrototype import Title


class Text(object):
    """1111"""


prototype = Title()
prototype.register('bird', Text())

owl = prototype.clone('bird', {'name': 'Owl'})
print(type(owl), owl.name)  # <class '__main__.Bird'> Owl

duck = prototype.clone('bird', {'name': 'Duck'})
print(type(duck), duck.name)  # <class '__main__.Bird'> Duck
