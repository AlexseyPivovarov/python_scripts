import weakref
class Register:
    __register=[]
    @classmethod
    def add(cls,obj):
        cls.__register.append(weakref.proxy(obj))
    @classmethod
    def get(cls,index):
        return cls.__register[index]


def register(init):
    def wrap(obj,*args,**kwargs):
        Register.add(obj)
    init(obj,*args,**kwargs)
    return wrap

class Owner:
    @register
    def __init__(self,a,b):
        print("init")
        self.a = a
        self.b = b

    def __str__(self):
        return "{}_{}".format(self.a,self.b)

for i,j in enumerate(range(10,20)):
    a=Owner(i,j)
