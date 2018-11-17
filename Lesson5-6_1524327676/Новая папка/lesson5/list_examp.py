list_ =[1,2,3]
list_.append(list_)
for item in list_:
    print(item)
    if type(item)==list:
        for i in item:
            print(i)
    if isinstance(item, list):
        for i in item:
            print(i)
