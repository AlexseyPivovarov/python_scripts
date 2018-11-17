a=-5
def f():
    global a
    a=555
    print("local",b)

f()
print("global",a)
