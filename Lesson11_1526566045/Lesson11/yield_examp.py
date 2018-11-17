from test_decorator import test_f_time
lst1 = (i for i in range(10000000))
lst2 = (i for i in range(10000000))
def my_sort(lst1=lst1,lst2=lst2):
    a=next(lst1)
    b=next(lst2)
    while True:
        if a<=b:
            yield a
            try:
                a=next(lst1)
            except:
                flag=1
                break
        else:
            yield b
            try:
                b=next(lst2)
            except:
                flag=0
                break
    if flag:
        for item in lst2:
            yield item
    else:
        for item in lst1:
            yield item
@test_f_time
def sort_test(lst1,lst2):
    return [item for item in my_sort(lst1,lst2)]
sort_test(lst1,lst2)
lst1 = [i for i in range(10000000)]
lst2 = [i for i in range(10000000)]
@test_f_time
def my_sort_2(lst1=lst1,lst2=lst2):
    return sorted(lst1+lst2)
