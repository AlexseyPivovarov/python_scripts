from os import system, name
cls = "cls" if name == "nt" else "clear"


#  -------------------------------------------- импорт ----------------------------------------------------------------
def reading():
    base = {}

    with open("telephone_book.txt", "r", encoding="UTF-8") as f:
        while EOFError:
            line = f.readline()
            if line == "":
                break
            contact = line.split("¿")[0].split("¦")[0]
            teg = line.split("¿")[0].split("¦")[1]
            data = line.split("¿")[1]
            if teg == "name":
                for item in data[:-2].split("¡"):
                    key = item.split("¦")[0]
                    value = item.split("¦")[1]
                    base.setdefault(contact, {}).setdefault("name", {}).update({key: value})
            else:
                base.setdefault(contact, {}).setdefault(teg, []).extend(data[:-1].split("¡"))

        return base


try:
    database = reading()
except IOError:
    database = {
        "alexei": {
            "name": {"first_name": "Alexei", "second_name": "Pivovarov"},
            "tel ": ["36546341", "654654"],
            "mail": ["smaster@bigmir.net", "smaster@gmail.com"],
        },
        "nina": {
            "name": {"first_name": "Nina"},
            "tel ": ["5645464"],
            "mail": ["nina@bigmir.net"],
        },
        "inna": {
            "name": {"first_name": "Inna"},
            "tel ": ["5434654"],
            "mail": ["inna@bigmir.net"],
        },
    }


#  -------------------------------------------- експорт ---------------------------------------------------------------
def writing(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        with open("telephone_book.txt", "w", encoding="UTF-8") as f:
            for contact in database:
                f.write("{}¦name¿".format(contact))
                for teg in database[contact]["name"]:
                    f.write("{}¦{}¡".format(teg, database[contact]["name"][teg]))
                f.write("\n{}¦tel ¿{}".format(contact, "¡".join(database[contact]["tel "])))
                f.write("\n{}¦mail¿{}\n".format(contact, "¡".join(database[contact]["mail"])))
        return a
    return wrapper


#  --------------------------- словарь содержащий все текстовые выражения ---------------------------------------------
sey = {
    "ru": {
        "hi": "Вас приветствует телефонная книга версии 3.0!!!",
        "help": "Для вызова данной справки введите '/п'\n"
                "Для выхода из приложения - '/в'\n"
                "Для смены языка - '/я'\n"
                "Для просмотра всей книги - '/т'\n"
                "Для поиска либо создания нового контакта введите ключевые слова через пробел\n"
                "Режим редактирования станет доступен если результатом поиска будет единый контакт",
        "enter": "Ваши действия: ",
        "exit": "Всего доброго!",
        "name": "Имена",
        "tel ": "Тел  ",
        "mail": "Почта",
        "input_data": "Вы ввели:",
        "is_find": "Найдены следующие совпадения:",
        "none": "Совпадения не найдены!",
        "/d": "Для удаления выбраных контактов введите '/у'",
        "/r": "Для редактирования котакта введите '/р'",
        "/s": "Для сохранения котакта введите '/c'",
        "retry": "Невозможно сохранить контакт без имени",
        "confirm": "Подтвердите ваши намеренья [д/н]",
        "canceled": "Действие отменено",
        "help2": "Для добавления имени введите 'и', телефона - 'т', почты - 'п', затем данные\n"
                 "Для замены - номер поля, затем новые данные\n"
                 "Для удаления - номер поля, затем '/у'\n"
                 "Для выхода - 'в'",
        "input2": "Ключ: ",
        "input": "Данные: ",
        "first_name": "имя",
        "second_name": "фамилия",
        "other1": "прочее1",
        "other2": "прочее2",
        "other3": "прочее3",
        "other4": "прочее4",
        "other5": "прочее5",
        "other6": "прочее6",
        "other7": "прочее7",
        "other8": "прочее8",
        "other9": "прочее9",
        "other10": "прочее10",
    },

    "en": {
        "hi": "Welcome to the phone book, version 3.0!!!",
        "help": "To access this help, enter '/h'\n"
                "To exit the application - '/e'\n"
                "To change the language - '/l'\n"
                "To view the entire book - '/t'\n"
                "To search for or create a new contact, enter the keywords with a space\n"
                "The editing mode will be available if the result of the search is a single contact",
        "enter": "Your actions: ",
        "exit": "Goodbye!",
        "name": "Names",
        "tel ": "Tel  ",
        "mail": "Mail ",
        "input_data": "you entered:",
        "is_find": "The following matches are found:",
        "none": "No matches found!",
        "/d": "To delete the selected contacts, enter '/d'",
        "/r": "To edit the contact, enter '/r'",
        "/s": "To save the contact, enter '/s'",
        "retry": "Unable to save contact without name",
        "confirm": "Confirm your intentions [y/n]",
        "canceled": "Action canceled",
        "help2": "To add a name, enter 'n', phone - 't', mail - 'm', then the data\n"
                 "To replace - the field number, then the new data\n"
                 "To removing - the field number, then '/d'\n"
                 "To exit - 'e'",
        "input2": "The key: ",
        "input": "Data: ",
        "first_name": "first name",
        "second_name": "second name",
        "other1": "other1",
        "other2": "other2",
        "other3": "other3",
        "other4": "other4",
        "other5": "other5",
        "other6": "other6",
        "other7": "other7",
        "other8": "other8",
        "other9": "other9",
        "other10": "other10",

    }
}


#  ---------------------------- иницыализацыя глобальной переменной состояния языка -----------------------------------
f = open("config.ini", "r")
lang = f.read()[8:10]
f.close()


#  ---------------------------------------------- просто коратин ------------------------------------------------------
def coros(func):
    def wrapper(*args, **kwargs):
        return next(func(*args, **kwargs))
    return wrapper


#  -------- генератор синхронизации значения глобальной переменной языка с областью видимости главной функции ---------
@coros
def language(*args):
    while True:
        yield lang


#  ----------------------------- функция смены значения глобальнй переменной языка ------------------------------------
def change_lang(*args):
    global lang
    if lang == "ru":
        lang = "en"
        with open("config.ini", "w") as file:
            file.write('lang = "en"')
    else:
        lang = "ru"
        with open("config.ini", "w") as file:
            file.write('lang = "ru"')


#  ----------------------------------------- функция вызова справки ---------------------------------------------------
def help_(*args):
    system(cls)
    print(sey[lang]["help"])


#  ----------------------------- функция отображения базы телефонного справочника -------------------------------------
#  -----------------------принимает список ключей контактов базы телефонного справочника ------------------------------
#  ---------------- при вызове без аргумента отображает текущую базу телефонного справочника --------------------------
def show_oll(key_list="default"):
    if key_list == "default":
        key_list = database.keys()
    for contact in key_list:
        print(sey[lang]["name"], end="|  ")
        for item in database[contact]["name"].values():
            print(item, end="  ")
        print(end="\n")
        print(sey[lang]["tel "], end="|  ")
        for number in database[contact]["tel "]:
            print(number, end="  ")
        print(end="\n")
        print(sey[lang]["mail"], end="|  ")
        for mail in database[contact]["mail"]:
            print(mail, end="  ")
        print(end="\n")
        print("---------------------------------------------")


#  -------------------------------------- функция отображения контакта ------------------------------------------------
#  -------------------------------------- принимает структуру котакта -------------------------------------------------
def show_contact(contact):
    print(sey[lang]["name"], end="|  ")
    for item in contact["name"].values():
        print(item, end="  ")
    print(end="\n")
    print(sey[lang]["tel "], end="|  ")
    for number in contact["tel "]:
        print(number, end="  ")
    print(end="\n")
    print(sey[lang]["mail"], end="|  ")
    for mail in contact["mail"]:
        print(mail, end="  ")
    print(end="\n")
    print("---------------------------------------------")


#  ------------------ функция поиска совпадений полученых данных с данными в базе справочника -------------------------
#  ----------------------- принимает структуру данных такого же типа как и база словаря -------------------------------
#  ----------------------- возвращает список ключей котактов в которых были совпадения --------------------------------
def search_in_base(arg):

    #  ---- функция ищет совпадение в данных под ключами ["name"] ----
    def search_in_names(finder, contact):
        for to_find in finder:
            for in_find in contact:
                if finder[to_find].lower() in contact[in_find].lower():
                    return True
        return False

    #  ---- функция ищет совпадение в данных под ключами ["tel "] ----
    def search_in_tel(finder, contact):
        for to_find in finder:
            for in_find in contact:
                if to_find in in_find:
                    return True
        return False

    #  ---- функция ищет совпадение в данных под ключами ["mail"] ----
    def search_in_mail(finder, contact):
        for to_find in finder:
            for in_find in contact:
                if to_find.lower() in in_find.lower():
                    return True
        return False

    #  -------------------- основной цыкл функции --------------------
    res = []
    for contact_ in database:
        if (search_in_names(arg["name"], database[contact_]["name"])
                or search_in_tel(arg["tel "], database[contact_]["tel "])
                or search_in_mail(arg["mail"], database[contact_]["mail"])):
            res.append(contact_)
    return res


#  ------------------------------ функция сохранения контакта в базу справочника --------------------------------------
#  ----------------------- принимает структуру данных такого же типа как и база словаря -------------------------------
@writing
def save_contact(temp):
    try:
        check = temp["name"]["first_name"]
    except KeyError:
        print(sey[lang]["retry"])
        return
    else:
        confirm = input(sey[lang]["confirm"]).lower()
        if confirm == "y" or confirm == "д":
            database[check + temp["name"].get("second_name", " ")] = temp
            return
        else:
            print(sey[lang]["canceled"])
            return


#  -------------------------------- функция удаления контакта с базы справочника --------------------------------------
#  ------------------------------ принимает список ключей соответствующих контактов -----------------------------------
@writing
def del_contact(result):
    confirm = input(sey[lang]["confirm"]).lower()
    if confirm == "y" or confirm == "д":
        for item in result:
            database.pop(item)
        return
    else:
        print(sey[lang]["canceled"])
        return


#  ------------------------------ функция редактирования контакта в базе справочника ----------------------------------
#  ----------------------------------- принимает ключ соответствующего контакта ---------------------------------------
@writing
def edit_contact(contact):

    #  ----------------- функция замены и удаления данных ---------------------
    def init_item(a, b, c):
        if c != "/у" and c != "/d":
            database[contact][a][b] = c
        else:
            database[contact][a].pop(b)

    #  --------------- функция добавления данных в новые поля -----------------
    def add_name(new_name):
        if not ("first_name" in database[contact]["name"]):
            database[contact]["name"]["first_name"] = new_name
        elif not ("second_name" in database[contact]["name"]):
            database[contact]["name"]["second_name"] = new_name
        else:
            database[contact]["name"]["other{}".format(len(database[contact]["name"]) - 1)] = new_name

    #  ------------------------ основной цыкл функции -------------------------
    while True:
        system(cls)
        restruct = {}
        coin = 0

        #  ------------------------ вывод интерфейса --------------------------
        print("---------------------------------------------")

        for key in database[contact]["name"]:
            coin += 1
            print("{1}: {2}->({0}) ".format(coin, sey[lang].get(key, key), database[contact]["name"][key]), end=" ")
            restruct[str(coin)] = lambda item, ikey=key: init_item("name", ikey, item)

        print(end="\n")
        print("---------------------------------------------")

        for i, items in enumerate(database[contact]["tel "]):
            coin += 1
            print("{1}->({0}) ".format(coin, items), end=" ")
            restruct[str(coin)] = lambda item, j=i: init_item("tel ", j, item)

        print(end="\n")
        print("---------------------------------------------")

        for i, items in enumerate(database[contact]["mail"]):
            coin += 1
            print("{1}->({0}) ".format(coin, items), end=" ")
            restruct[str(coin)] = lambda item, j=i: init_item("mail", j, item)

        print(end="\n")
        print("---------------------------------------------")
        print(sey[lang]["help2"])

        #  - добавление в функциональный словарь функций с нецыфровыми ключами -
        restruct["n"] = lambda item: add_name(item)
        restruct["t"] = lambda item: database[contact]["tel "].append(item)
        restruct["m"] = lambda item: database[contact]["mail"].append(item)
        restruct["и"] = lambda item: add_name(item)
        restruct["т"] = lambda item: database[contact]["tel "].append(item)
        restruct["п"] = lambda item: database[contact]["mail"].append(item)

        #  --------------- запрос и обработка данных пользователя --------------
        func = ""
        while func == "" or not (func in restruct):
            func = input(sey[lang]["input2"])
            if func == "в" or func == "e":
                return
        arg = ""
        while arg == "":
            arg = input(sey[lang]["input"])
            if arg == "в" or arg == "e":
                return
        restruct[func](arg)


if __name__ == '__main__':
    reading()
