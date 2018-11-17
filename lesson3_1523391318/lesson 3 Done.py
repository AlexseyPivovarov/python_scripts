text = input("Введите строку: ")
index = -int(len(text) // 2)
outText = text[index:] + text[:index]
print(outText)
