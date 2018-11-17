import random
e = [i for i in range(100) if i%2==0]
print(e)
z = [[j for j in range(5)] for i in range(5) ]
print(z)
x = [ i for i in range(5) for j in range(i)]
print(x)
y = [i if i%2 else 0 for i in [random.randint(1,100) for _ in range(10)]]
print(y)
