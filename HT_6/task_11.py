"""http://www.pythonabc.com/best-way-count-instances-python-class/"""


class MyClass:
    num_of_instamces = 0

    @classmethod
    def countInstances(cls):
        cls.num_of_instamces += 1

    @classmethod
    def getNumInstances(cls):
        print(cls.num_of_instamces)

    def __init__(self):
        self.countInstances()


class Derived(MyClass):
    num_of_instamces = 0

    def __init__(self):
        MyClass.__init__(self)


b1 = MyClass()
b2 = MyClass()
d1 = Derived()
d2 = Derived()
d3 = Derived()
b1.getNumInstances()
MyClass.getNumInstances()
d1.getNumInstances()
Derived.getNumInstances()
