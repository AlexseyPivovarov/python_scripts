from test_decorator import test_f_time
a=[i for i in range(10000)]
b=[i for i in range(10000)]

@test_f_time
def q_sort(lst1, lst2):
    return sorted(lst1+lst2)
@test_f_time
def w_sort(lst1,lst2):
    a=[0 for _ in range(len(lst1)+len(lst2))]
    i=0
    j=0
    k=0
    while i<len(lst2)-1 or j<len(lst1)-1:
        if lst2[i]>lst1[j]:
            a[k]=lst1[j]
            if j<(len(lst1)-1):
                j+=1
        else:
            a[k]=lst2[i]
            if i<(len(lst2)-1):
                i+=1
        k+=1
    return a
print(w_sort(a,b)[-3:])
