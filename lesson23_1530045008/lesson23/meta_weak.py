import weakref
class ARegister(type):
    __istance = weakref.WeakValueDictionary()

    def __init__(cls,*args,**kwargs):
        print("init_type")
        super().__init__(*args,**kwargs)

    def __call__(cls,*args,**kwargs):
        print('call_type')
        inst = super().__call__(*args,**kwargs)
        cls.__istance[id(inst)]=inst
        return inst
    def f(self):
        print("Ok")

    @classmethod
    def get_instance(cls):
        return cls.__istance

class B(metaclass=ARegister):
    def __init__(self):
        print("init_B")
    def g(self):
        print("G")

class C(B):
    pass

a=C()
a.g()



# v = A.get_instance()
# print(dir(v))
#
# print(list(v.items()))
# for i in range(5):
#     a[i]=i
# print(list(v.items()))
