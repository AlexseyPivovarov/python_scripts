a= [[i+j for i in range(3)] for j in range(19,23)]

a=[]
for k,j in enumerate(range(19,23)):
    a.append([])
    for i in range(3):
        a[k].append(i+j)


a=[1,2,3,4]
b=["10","11","12","13","19","20"]
c=zip(a,b)
print(c)
# for i,j in zip(a,b):
#     print(i,j)
