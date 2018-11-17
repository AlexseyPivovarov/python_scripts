from random import randint, choices

# Создаю рандомную строку
words = "".join(choices("abcdefghijklm nopqrstuvwxyz абвгдеёжзийклмнопр стуфхцчшщъыьэюя", k=randint(1, 100)))
print("Случайный набор символов:", words)
# Основной алгоритм программы
out = {char: [words.count(char), round(100 / len(words) * words.count(char), 2)] for char in words}
# Вывод результата
[print("{} = {} ({}%)".format(key, out[key][0], out[key][1])) for key in out]
