info = [
    'A11F12',
    'C11a14',
    'B11F13',
    'A12a14'
]
def key_sort(item):
    return item[0]+item[3]
av = lambda item:item[3]+item[0]

print(sorted(info,key=av))
print(sorted(info,key=lambda item:item[0]+item[3]))
print(sorted(info,key=key_sort))

print(av("H11G78"))
