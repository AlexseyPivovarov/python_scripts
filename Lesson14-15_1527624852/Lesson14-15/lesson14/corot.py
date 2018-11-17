def coros(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper
@coros
def infinity():
    a=yield
    while a:
        tmp = a
        a = yield a
        if a is None:
            a = tmp
        print("yield a = {}".format(a))
        a-=1
f = infinity()
a=f.send(5)
ff = infinity()
ff.send(20)
for i,j in zip(f,ff):
    print("global i = {} j= {}".format(i,j))
    if i==1:f.send(5)
    if j==1:ff.send(20)
    input()
