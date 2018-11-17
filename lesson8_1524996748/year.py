def is_year_leap(year):
    return True if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else False


def main():
    while True:
        try:
            year = int(input("Введите год: "))
        except:
            continue
        break
    print("Год высокосный") if is_year_leap(year) else print("Год невысокосный")


main()
