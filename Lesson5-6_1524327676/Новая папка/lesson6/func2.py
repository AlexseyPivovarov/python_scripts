def func(b,a=1):
    if b<a:
        b,a=a,b
    summa=0
    for i in range(a,b+1):
        summa+=i
    return summa
for i in range(11):
    print("summa {0} = {1}".format(i, func(i)))
