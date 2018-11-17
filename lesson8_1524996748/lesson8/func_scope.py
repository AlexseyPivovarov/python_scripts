a=5
def f(a):
    print(a)
def f1():
    print(a)
def f2():
    a=77
    def f3():
        print(a)
    f3()
b = 10
def f():
    global b
    b=b+12
    print("local b",b)
f()
print("global",b)
