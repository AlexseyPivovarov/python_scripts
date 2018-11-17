from random import randint
from lib import vocabulary


# Создаю рандомную строку
word = vocabulary[randint(0, len(vocabulary))]
print("Случайное слово:", word)
# Основной алгоритм программы
out = {}
for char in word:
    out[char] = out.get(char, 0) + 1
# Вывод результата
[print("{} = {}".format(key, out[key])) for key in out]

