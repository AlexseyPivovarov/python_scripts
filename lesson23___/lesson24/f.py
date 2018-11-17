class A:
    pass
a=A()
for i in range(5):
    name = input("name attr->")
    if not hasattr(a,name):
        setattr(a,name,input("attr value->"))

print(dir(a))
