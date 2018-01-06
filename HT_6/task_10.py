class C1:
    def __init__(self, a):
        self.a = a


class C2:
    def change_c1_a(self, c1):
        c1.a = 5


o1 = C1(3)
o2 = C2()
o2.change_c1_a(o1)
print(o1.a)
