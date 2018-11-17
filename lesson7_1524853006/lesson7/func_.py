def func(obj):
    rez = obj(2,5)
    print(rez)
def f2(a,b):
    return a-b
def f1(a,b):
    return a+b
func(f1)
func(f2)
