a=input("First->")
print("a=",a, type(a))
try:
    a = int(a)
except:
    try:
        a= float(a)
    except:
        pass
if a:
    print("Ok")
else:
    print("Ups")
print("GoodBye")
