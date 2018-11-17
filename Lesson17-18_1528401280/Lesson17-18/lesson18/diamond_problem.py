class Foo:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get(self):
        return self.a+self.b
class Boo(Foo):
    def __init__(self,a,b):
        self.c = a
        self.d = b
        super().__init__("aaa","bbb")
class Coo(Boo,Foo):
    def __init__(self,a,b):
        self.m = a
        self.n = b
a =Coo(1,2)
