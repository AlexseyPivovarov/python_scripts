from random import randint
# создаю строку содержащие все символы учавствующие в шифровании
codWord = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"


# Функция шифрует сивол за шифром Цезаря
# принимает str и int, возвращает str
def move_char(char, key):
    index = codWord.find(char)
    if 0 <= index < 26:
        return codWord[(index + key) % 26]
    elif 26 <= index < 52:
        return codWord[(index - 26 + key) % 26 + 26]
    elif 52 <= index < 85:
        return codWord[(index - 52 + key) % 33 + 52]
    elif 85 <= index < 118:
        return codWord[(index - 85 + key) % 33 + 85]
    elif index == -1:
        return char


# Функция дешифрует сивол за шифром Цезаря
# принимает str, int, int; возвращает str
def de_move_char(char, en_key, ru_key):
    index = codWord.find(char)
    if 0 <= index < 26:
        return codWord[(index + 26 - en_key) % 26]
    elif 26 <= index < 52:
        return codWord[((index - en_key) % 26) + 26]
    elif 52 <= index < 85:
        return codWord[((index - ru_key - 19) % 33) + 52]
    elif 85 <= index < 118:
        return codWord[((index - ru_key - 19) % 33) + 85]
    elif index == -1:
        return char


# функция осуществляет поиск первого латинского символа
# принимает list, возвращает индекс символа в списке либо -1 если такового нет
def find_en_key_index(out_word):
    index = 0
    flag = True
    for i in range(len(out_word)):
        index = i
        if codWord[:52].find(out_word[index]) == -1:
            continue
        else:
            flag = False
            break
    return index if not flag else -1


# функция осуществляет поиск первого символа киррилици
# принимает list, возвращает индекс символа в списке либо -1 если такового нет
def find_ru_key_index(out_word):
    index = 0
    flag = True
    for i in range(len(out_word)):
        index = i
        if codWord[52:].find(out_word[index]) == -1:
            continue
        else:
            flag = False
            break
    return index if not flag else -1


# функция маскировки ключа в зашифрованом слове
# принимает list и int возвращает string
def hide_key(word, key):
    # определяю индекс первого латинского символа в слове
    en_index = find_en_key_index(word)
    if en_index != -1:
        # если таков символ найден, за ним вставляю ключ в виде латинского символа
        word.insert((en_index + 1), codWord[26 + ((key + 7) % 26)])
    # все тоже самое, но для ключа розшифровки киррилици
    ru_index = find_ru_key_index(word)
    if ru_index != -1:
        word.insert((ru_index + 1), codWord[85 + ((key + 13) % 33)])
    return word


# главная функция кодирования слова за заданным ключом
# принимает string и int, возвращает string
def codding(word):
    while True:
        key = randint(1, 857)
        # проверка на кратность ключа
        if key % 26 == 0 or key % 33 == 0:
            continue
        else:
            break
    # генерирую список символов из слова которое шифрую, сдвигая их на размер ключа по алфавиту
    word = [move_char(char, key) for char in word]
    # шифрую ключ в списке
    word = hide_key(word, key)
    # собираю строку
    return "".join(word)


# главная функция декодирования слова
# принимает string, возвращает string
def decoding(word):
    # генерирую список со строки
    word = [i for i in word]
    # нахожу и извлекаю ключ шифрования киррилици
    ru_index = find_ru_key_index(word)
    ru_key = (codWord.index(word.pop(ru_index + 1)) - 65) % 33 if ru_index != -1 else 0
    # нахожу и извлекаю ключ шифрования латиници
    en_index = find_en_key_index(word)
    en_key = (codWord.index(word.pop(en_index + 1)) - 7) % 26 if en_index != -1 else 0
    # генерирую список символов из слова которое дешифрую, сдвигая их на размер ключа по алфавиту в обратную сторону
    word = [de_move_char(char, en_key, ru_key) for char in word]
    return "".join(word)


def main():
    word = input("Введите строку для шифрования: ")
    coded = codding(word)
    print("После шифрования:", coded)
    print("После дешифрования", decoding(coded))


main()
