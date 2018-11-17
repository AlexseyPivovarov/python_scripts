class Register:
    __register = []
    @classmethod
    def add(cls,obj):
        cls.__register.append(obj)
    @classmethod
    def __getitem__(cls,index):
        return cls.__register[index]
    @classmethod
    def get(cls,index):
        return cls.__register[index]

class Foo:
    def __new__(cls,*args,**kwargs):
        obj = super().__new__(cls)
        Register.add(obj)
        return obj
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return "a={},b={}".format(self.a,self.b)

for i,j in enumerate(range(10,20)):
    a=Foo(i,j)

for i in range(10):
    print(Register()[i])
