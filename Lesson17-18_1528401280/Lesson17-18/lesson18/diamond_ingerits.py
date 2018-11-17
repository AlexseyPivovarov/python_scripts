class Foo:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get(self):
        return self.a+self.b
class Boo:
    def __init__(self,c,d):
        self.c = c
        self.d = d
        # super().__init__('aaa', 'bbb')
    def get(self):
        return self.c+self.d
class Coo(Foo,Boo):
    def __init__(self,a,b):
        self.e = a
        self.f = b
        # super().__init__('ccc','ddd')
        Boo.__init__(self,12,17)
        Foo.__init__(self,15,10)
a = Coo('eee','fff')
print(Coo.__mro__)
print(a.get())
print(a.a)
print(a.d)
