#Одновременное присвоение значение двум переменным
a, i = 12, 56
#Обмен значениями без использования буферной переменной
a,i=i,a
#Пример с использованием буферной переменной
tmp=a
a=i
i=a
#Далее рассмотрен пример использования оператора ветвления if
a=int(input("Enter->"))
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")
print("Hello")


a=int(input(">"))
if 0<a<10:#a>0 and a<10
   print("ok")
elif 10<a<100:
   pass
#приведение типов int к bool
if bool(a)==True:
   print("ok")
#если int не равен 0 он всегда True
elif a:
   print("OK-OK")
else:
   print("no")

#но если мы сравним int с True, они равны только если
#переменная типа int равна 1, так как True - 1, a False -0
if a==True:
    print("True")
else:
    print("False")
