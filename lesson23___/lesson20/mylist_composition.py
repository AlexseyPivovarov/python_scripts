class MyTupleList:
    class __MyList:
        __a=3
        __b=4
        def __init__(self,e):
            self.__e = e
        def __str__(self):
            return "class MyList {}".format(self.__e)
        def set__e(self,value):
            if (value>100):
                raise ValueError
            self.__e = value


    def __init__(self, a):
        self.a=MyTupleList.__MyList(a)
    def set_e(self,value):
        self.a.set__e(value)

    def __str__(self):
        return  "class MyTupleList {}".format(self.a)

foo = MyTupleList(10)
print(foo)
foo.set_e(99)
print(foo)
