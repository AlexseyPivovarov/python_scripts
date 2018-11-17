class Foo:
    a=1
    b=2
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __iter__(self):
        yield self.a
        yield self.b
        # return (item for item in (self.a,self.b,))
    def generator(self):
        return iter(self)
class FooFoo(Foo):
    def __init__(self,*args):
        super().__init__(args[0],args[1])
        self.d = args[2]
    def __iter__(self):
        yield from super().__iter__()
        yield self.d

childFoo = Foo(7,10)
foofoo = FooFoo(*childFoo,5)
for item in foofoo:
    print(item)
