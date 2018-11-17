class Foo:
    # def __getattribute__(self,name):
    #     __dict__ = super().__getattribute__('__dict__')
    #     if name == "__dict__":
    #         return {'__dict__':{}}
    #     if name in __dict__:
    #         return super().__getattribute__(name)
    #     return "Hello!"
    def __setattr__(self,name,value):
        __local__ = ['a','add','c']
        if name in __local__:
            self.__dict__[name]=value


#создаю экземпляр класса
a=Foo(5)
b=Foo(5)
#создаю атрибут класса add
a.add=545
b.ddd=10
print(a.a)
print(a.add)
print(b.a)
# setattr(a,"addd","Hello")
# print(a.addd)
# print(getattr(a,"addd"))
# print(hasattr(a,"addd"))
# print(hasattr(a,"ddd")
