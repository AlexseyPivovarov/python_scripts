b=[]
def f():
    a=77
    b=133
    def f1():
        global a
        b=5687
        a=333
        print("local in local f1",a)
        def f2():
            nonlocal b
            b=555
            print("local in local f2",b)
        f2()
        print("local in local f1 b",b)
    f1()
    print("local a", a)
    print("local b", b)
a=7
f()
print("global",a)
print(b)
