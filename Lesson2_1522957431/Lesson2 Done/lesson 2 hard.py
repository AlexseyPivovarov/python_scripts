print("Определение четвертей которые пересекает отрезок заданный двумя точками")
# input block
number = []
stop = 0
for dynamicText in ['x для первой', 'y для первой', 'x для второй', 'y для второй']:
    while True:
        temp = input('Введите координату {} точки, либо "e" для выхода: '.format(dynamicText))
        if temp == "e":
            stop = 1
            break
        try:
            number.append(int(temp))
            break
        except:
            try:
                number.append(float(temp))
                break
            except:
                print("Вы ввели некоректные данные, попытайтесь снова")
    if stop:
        break
# logical and output block
if not stop:
    print(number)
    x1, y1, x2, y2 = number
    text2 = "Отрезок"
    if x1 == x2 and y1 == y2:
        text2 = "Нулевой отрезок"
    if not x1 and not y1 and not x2 and not y2:
        print("{} находится в центре координат".format(text2))
    elif not y1 and not y2:
        if x1 >= 0 <= x2:
            text4 = "OX"
        elif x1 <= 0 >= x2:
            text4 = "-OX"
        else:
            text4 = "X и проходит через центр"
        print("{} находится на оси {}".format(text2, text4))
    elif not x1 and not x2:
        if y1 >= 0 <= y2:
            text4 = "OY"
        elif y1 <= 0 >= y2:
            text4 = "-OY"
        else:
            text4 = "Y и проходит через центр"
        print("{} находится на оси {}".format(text2, text4))
    else:
        # some magic
        for index in range(4):
            if not number[index]:
                number[index] = number[(index + 2) % 4]
        signX, signY = number[0] / number[2], number[1] / number[3]
        # если в одной четверти
        if signX > 0 < signY:
            if number[0] > 0 < number[1]:
                text = "в первой"
            elif number[0] < 0 < number[1]:
                text = "во второй"
            elif number[0] < 0 > number[1]:
                text = "в третей"
            else:
                text = "в четвертой"
            print("{} находится {} четверти".format(text2, text))
        # если в смежных четвертях
        elif signX > 0 > signY:
            if number[0] > 0:
                text = "первой и четвертой"
            else:
                text = "второй и третей"
            print("Отрезок находится в смежных {} четвертях".format(text))
        elif signX < 0 < signY:
            if number[1] > 0:
                text = "первой и второй"
            else:
                text = "третей и четвертой"
            print("Отрезок находится в смежных {} четвертях".format(text))
        # если отрезок в диагональных четвертях
        else:
            if y1 < 0:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            tgAB = (abs(x1) + abs(x2)) / (abs(y1) + abs(y2))
            tgAO = abs(x1) / abs(y1)
            if signX > 0:
                text = "первой и третей"
                if tgAB > tgAO:
                    text3 = "смежной второй четверти"
                elif tgAB < tgAO:
                    text3 = "смежной четвертой четверти"
                else:
                    text3 = "проходит через центр"
            else:
                text = "второй и четвертой"
                if tgAB > tgAO:
                    text3 = "смежной первой четверти"
                elif tgAB < tgAO:
                    text3 = "смежной третей четверти"
                else:
                    text3 = "проходит через центр"
            print("Отрезок находится в диагональных {} четвертях и {}".format(text, text3))
print("Готово!")
