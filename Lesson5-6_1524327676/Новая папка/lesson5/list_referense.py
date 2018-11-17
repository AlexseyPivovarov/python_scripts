from copy import deepcopy
a = [1,2,3,4,5,[77,88,99]]
b=deepcopy(a)
b[-1][0]="abc"
print(a)
