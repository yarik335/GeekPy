class Thing:
    pass


class Thing2:
    letters = 'abc'


class Thing3:
    letters = 'xyz'


example = Thing()
print(Thing2.letters)
print(Thing3.letters)
print(type(Thing))
print(type(example))
