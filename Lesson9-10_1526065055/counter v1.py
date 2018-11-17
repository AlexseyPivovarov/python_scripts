from random import randint, choice


# Функция подсчёта количевства символов в строке
def counter(text):
    text = text.lower()
    base = {char: [0, 0] for char in text}
    for char in text:
        base[char][0] += 1
        base[char][1] = round(base[char][1] + 100 / len(text), 2)
    return base


if __name__ == '__main__':
    # генерация случайной строки
    words = "".join([choice([chr(randint(97, 122)), chr(randint(1072, 1103))]) for _ in range(randint(1, 100))])
    print("Случайный набор символов:", words)
    # подсчёт символов
    stat = counter(words)
    # вывод результата
    for key in stat:
        print("{} = {} ({}%)".format(key, stat[key][0], stat[key][1]))
