class Foo:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return Foo(self.a + other.a)
    def __radd__(self,other):
        self.a+=other.a
a = Foo(1)
b = Foo(3)
c=a+b
a+=b
