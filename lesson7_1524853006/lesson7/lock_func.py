def f(n):
    def f1(b):
        return n+b
    return f1

obj = f("14")
obj2 = f("23")
names = ["15","16","68","67"]
for  i in names:
    print(obj(i))
    print(obj2(i))


f(45)
