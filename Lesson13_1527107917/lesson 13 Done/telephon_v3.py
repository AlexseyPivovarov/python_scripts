from helpers_ import *
from os import system, name
cls = "cls" if name == "nt" else "clear"


def mainloop():

    #  -------------------------------- вывод приветствия старте справочника ------------------------------------------
    def start():
        system(cls)
        print(sey[language()]["hi"])
        print(sey[language()]["help"])
    cash_function = start  # Кеширование приветствия
    cash_function()  # Вывод приветствия
    result = []
    temp = {
        "name": {},
        "tel ": [],
        "mail": [],
    }

    #  ---------------------------- вход в основной цыкл и запрос действий от пользователя ----------------------------
    while True:
        data = ""
        while not data or data == "@":  # игнорирование пустого ввода и исключений
            data = input(sey[language()]["enter"])  # Точка ввода

        #  -------------------------------------- проверка на ключ выхода ---------------------------------------------
        if data == '/в' or data == '/e':
            return print(sey[language()]["exit"])  # Выход с программы

        #  ----------------------------------- проверка на ключ смены языка -------------------------------------------
        elif data == '/я' or data == '/l':
            change_lang()  # Смена языка
            # вызов кеш функции для повтора предыдущего действия с новым значением глобальной переменной языка
            cash_function()
            continue

        #  ---------------------------------- проверка на ключ вызова справки -----------------------------------------
        elif data == '/п' or data == '/h':
            help_()  # Вывод справки
            cash_function = help_
            continue

        #  ----------------------- проверка на ключ отображения всего справочника -------------------------------------
        elif data == '/т' or data == '/t':
            def show():
                system(cls)
                show_oll()  # Вывод всего справочника
            show()
            cash_function = show
            continue

        #  ------------- ответвление на проверку ключей вызова функций на оброботку данных ----------------------------
        if temp["name"] or temp["tel "] or temp["mail"]:
            if data == '/с' or data == '/s':
                save_contact(temp)
                continue
            elif result:
                if data == '/у' or data == '/d':
                    del_contact(result)
                    continue
                elif len(result) == 1:
                    if data == '/р' or data == '/r':
                        edit_contact(result[0])
                        continue

        #  -------------------- структурирование входнх данных в структкру котакта ------------------------------------
        temp = {
            "name": {},
            "tel ": [],
            "mail": [],
        }

        temp_list = []

        #  распознование почты, телефонов и заполнения структуры контакта в соответственные поля
        for item in data.split():
            if item.count("@") == 1:
                temp["mail"].append(item)
            elif item.isdigit() or (item[1:].isdigit() and item[0] == "+"):
                temp["tel "].append(item)
            else:
                temp_list.append(item)

        #  заполнение поля ["name"] в структуре контакта
        for number, item in enumerate(temp_list):
            if number == 0:
                temp["name"]["first_name"] = item
            elif number == 1:
                temp["name"]["second_name"] = item
            else:
                temp["name"]["other{}".format(number - 1)] = item

        #  ---------------------------------- поиск по базе справочника -----------------------------------------------
        result = search_in_base(temp)

        #  ----------------------------------- обновление интерфейса --------------------------------------------------
        def interface():
            system(cls)
            print(sey[language()]["input_data"])
            show_contact(temp)
            if result:
                print(sey[language()]["is_find"])
                print()
                show_oll(result)
                print(sey[language()]["/d"])
                if len(result) == 1:
                    print(sey[language()]["/r"])
            else:
                print(sey[language()]["none"])
            print(sey[language()]["/s"])
        interface()
        cash_function = interface


if __name__ == '__main__':
    mainloop()

