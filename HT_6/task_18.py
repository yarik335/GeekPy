class MyClass1:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2


class MyClass2(MyClass1):
    def __init__(self, a1, a2, a3):
        MyClass1.__init__(self,a1, a2)
        self.a3 = a3


class MyClass3(MyClass2):
    def __init__(self, a1, a2, a3, a4):
        MyClass2.__init__(self, a1, a2, a3)
        self.a4 = a4


o1 = MyClass1(1, 2)
o2 = MyClass2(1, 2, 3)
o3 = MyClass3(1, 2, 3, 4)
print(o1.__dict__)
print(o2.__dict__)
print(o3.__dict__)
