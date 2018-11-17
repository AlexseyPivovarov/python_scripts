from random import randint
# создаю строку содержащие все символы учавствующие в шифровании
codWord = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"


# функция создаёт строку на подобии codWord для шифрования но со сдвигом на размер ключа в четырех диапазонах символов
# принимает занчение int, возвращает строку
def cod_key(key):
    key_list = []
    key_list.extend([codWord[(i + key) % 26] for i in range(26)])
    key_list.extend([codWord[(i - 26 + key) % 26 + 26] for i in range(26, 52)])
    key_list.extend([codWord[(i - 52 + key) % 33 + 52] for i in range(52, 85)])
    key_list.extend([codWord[(i - 85 + key) % 33 + 85] for i in range(85, 118)])
    return "".join(key_list)


# функция создает строку на подобии codWord для дешифрования со сдвигом по двум ключам: для латиницы и кириллицы
# принимает два значения int, возвращает строку
def decode_key(en_key, ru_key):
    key_list = []
    key_list.extend([codWord[(i + en_key) % 26] for i in range(26)])
    key_list.extend([codWord[(i - 26 + en_key) % 26 + 26] for i in range(26, 52)])
    key_list.extend([codWord[(i - 52 + ru_key) % 33 + 52] for i in range(52, 85)])
    key_list.extend([codWord[(i - 85 + ru_key) % 33 + 85] for i in range(85, 118)])
    return "".join(key_list)


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
def hide_key(out_word, key):
    # определяю индекс первого латинского символа в слове
    en_index = find_en_key_index(out_word)
    if en_index != -1:
        # если таков символ найден, за ним вставляю ключ в виде латинского символа
        out_word.insert((en_index + 1), codWord[26 + ((key + 7) % 26)])
    # все тоже самое, но для ключа розшифровки киррилици
    ru_index = find_ru_key_index(out_word)
    if ru_index != -1:
        out_word.insert((ru_index + 1), codWord[85 + ((key + 13) % 33)])
    return out_word


# главная функция кодирования слова за заданным ключом
# принимает string и int, возвращает string
def codding(word, key):
    # проверка на кратность ключа
    if key % 26 == 0 or key % 33 == 0:
        key = randint(1, 25)
    # создаю строку на подобии codWord но со здвигом на ключ
    key_word = cod_key(key)
    # генерирую список символов из слова которое шифрую, заменяя символами из key_word по их индексу в codWord
    out_word = [key_word[codWord.find(char)] if codWord.find(char) != -1 else char for char in word]
    # шифрую ключ в списке
    out_word = hide_key(out_word, key)
    # собираю строку
    return "".join(out_word)


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
    # создаю строку на подобии codWord но со здвигом на ключ
    key_word = decode_key(en_key, ru_key)
    # генерирую список символов из слова которое дешифрую, заменяя символами из codWord по их индексу в key_word
    word = [codWord[key_word.find(char)] if codWord.find(char) != -1 else char for char in word]
    return "".join(word)


def main():
    word = input("Введите строку для шифрования: ")
    while True:
        try:
            key = int(input("Задайте ключ числом: "))
        except:
            continue
        break
    coded = codding(word, key)
    print("После шифрования:", coded)
    print("После дешифрования", decoding(coded))


main()
