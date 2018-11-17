d = {i:i+2**i for i in range(10)}
a={i+2**i:i for i in range(10)}
c=[i for i in range(10,20)]
e = {key:value for key, value in zip(c,d.items())}
print(e)

for  key in d:
    print (key)
for  value in d.values():
    print (value)
for item in d.items():
    print(item)
print(d.get(999))
