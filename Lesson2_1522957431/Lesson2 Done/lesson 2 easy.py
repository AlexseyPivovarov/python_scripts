print("Определение четверти положения точки заданными координатами")
# initialise variables
number = []
# input block
stop = 0
dynamicText = ['x', 'y']
for index in range(2):
    while True:
        number.insert(index, input('Введите координату {}, либо "e" для выхода: '.format(dynamicText[index])))
        if number[index] != "e":
            try:
                number[index] = int(number[index])
                break
            except:
                try:
                    number[index] = float(number[index])
                    break
                except:
                    print("Вы ввели некоректные данные, попытайтесь снова")
        else:
            stop = 1
            break
    if stop == 1:
        break
# output block
if stop == 0:
    x1 = number[0]
    y1 = number[1]
    # print("Вы ввели А({},{})".format(x1, y1))
    if x1 > 0:
        if y1 > 0:
            print("Ваша точка А({},{}) находится в первой четверти".format(x1, y1))
        elif y1 < 0:
            print("Ваша точка А({},{}) находится в четвертой четверти".format(x1, y1))
        else:
            print("Ваша точка А({},{}) находится на оси X".format(x1, y1))
    elif x1 < 0:
        if y1 > 0:
            print("Ваша точка А({},{}) находится во второй четверти".format(x1, y1))
        elif y1 < 0:
            print("Ваша точка А({},{}) находится в третей четверти".format(x1, y1))
        else:
            print("Ваша точка А({},{}) находится на оси X".format(x1, y1))
    else:
        if y1 != 0:
            print("Ваша точка А({},{}) находится на оси Y".format(x1, y1))
        else:
            print("Ваша точка А({},{}) находится в центре координат".format(x1, y1))
print("Готово!")

