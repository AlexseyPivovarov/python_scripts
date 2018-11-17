
import weakref
class Register:
    __register=[]
    @classmethod
    def register(cls,init):
        def wrapp(*args,**kwargs):
            cls.__register.append(id(weakref.proxy(args[0])))
            init(*args,**kwargs)
            print("Register {}".format(args[0]))
        return wrapp
    @classmethod
    def get(cls,index):
        return cls.__register[index]

class Owner:
    @Register.register
    def __init__(self,a,b):
        print("init")
        self.a = a
        self.b = b
    def __str__(self):
        return "{}_{}".format(self.a,self.b)

for i,j in enumerate(range(10,20)):
    Owner(i,j)

for i in range(10):
    print(Register.get(i))
