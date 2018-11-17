def time(func):
    def wrapper(*args):
        print(*args)
        from time import time
        start = time()
        a = func(*args)
        end = time()
        print("{} Time {}ms".format(func.__name__,round(end-start,6)))
        return a
    return wrapper
@time
def f(a,b):
    i = 1
    for j in range(a,b+1):
        i*=j
    return i
@time
def f1():
    i=1
    j=1
    while j<10000:
        i*=j
        j+=1
    return i
f(10,20)
f1()
