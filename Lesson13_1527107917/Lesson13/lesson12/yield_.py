def f(a):
    yield
    while a:
        yield a
        a-=1
    else:
        return 999

a = f(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
