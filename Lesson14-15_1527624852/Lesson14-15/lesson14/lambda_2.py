f = lambda item: [i for i in range(item)]
f_exp = lambda item: lambda low: item+low
c = f_exp(10)
print(c(21))
print(c(25))
print(c(27))
b = f_exp(77)(11)
a=f(5)
print(a)
