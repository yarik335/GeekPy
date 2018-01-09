class A:
    def __init__(self, a):
        self._a = a

    @staticmethod
    def add_values(a):
        return a+10

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value


o = A(12)
print(o.a)
print(o.add_values(o.a))
print(o.a)



