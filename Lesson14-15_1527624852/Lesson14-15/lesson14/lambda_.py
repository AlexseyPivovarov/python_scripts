lambdas = []
for i in range(10):
    lambdas.append((lambda b, i=i: b+i))
for j,val in zip(range(10),range(101,211)):
    print(lambdas[j](val))
a=zip(list(range(3)),list(range(101,211)))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))



# a=[1,2,3,4,6]
# a=iter(a)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
