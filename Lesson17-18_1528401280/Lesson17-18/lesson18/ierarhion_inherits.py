class Foo:
    def __init__(self,*args,**kwargs):
        self.__a = kwargs['master'] if 'master' in kwargs else args[0]
        # try:
        #     self.a = kwargs['master']
        # except:
        #     self.a = args[0]
        self.__b = kwargs['b']
    def get_a(self):
        return self.__a
class Boo(Foo):
    def __init__(self,*args,**kwargs):
        self.c = kwargs['c']
        self.d = kwargs['d']
        super().__init__(self,*args,**kwargs)
    def get_a(self):
        # return super().get_a()
        return Foo.get_a(self)
class Coo(Boo):
    def __init__(self,*args,**kwargs):
        self.e = kwargs['e']
        self.f = kwargs['f']
        super().__init__(self,*args,**kwargs)
    def get_a(self):
        # return Foo.get_a(self)
        return super().get_a()

coo = Coo(5,b=12,e=14,c=19,d=20,f=0)
print(Coo.__mro__)
