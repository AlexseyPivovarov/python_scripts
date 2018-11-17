class Foo:
    __child=[]
    def __init__(self, a,b):
        self.a = a
        self.b = b
        Foo.__child.append(self)
    def __str__(self):
        return "a={} b={}".format(self.a,self.b)
    def get_child(self):
        return len(Foo.__child)
    @classmethod
    def get_spirit_child(cls):
        return cls.__child
    def get_exp_child(self):
        return self.__child

class Boo(Foo):
    def __init__(self, a,b):
        Foo.__init__(self,a,b)
    def info(self):
        return "I'm Boo"


boo = Boo(77,99)
foo = Foo(1,1)

for elem in Foo.get_spirit_child():
    print(elem.info())
