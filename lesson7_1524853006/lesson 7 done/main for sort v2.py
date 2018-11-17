from random import randint


def time(func):
    def wrapper():
        from time import time
        start = time()
        a = func()
        end = time()
        print("{} time {}".format(func.__name__, round(end - start, 6)))
        return a
    return wrapper


# функция слияния двух списков со сменой порядка сортирования
# принимает два отсортированых по убыванию списка и возвращает новый отсортированый по возрастанию
def merge(first, second):
    return [first.pop() if (first and second and first[-1] < second[-1]) or (first and not second) else second.pop()
            for _ in range(len(first) + len(second))]


# функция сортировки списка алгоритмом слияния
# принимает несортированый список и ничего не возвращает но перезаписывает входящий в отсортированый по убыванию
def merge_sort(list_):
    len_ = len(list_)
    if len_ <= 1:
        return
    mid = len_ // 2
    first = list_[mid:]
    second = list_[:mid]
    merge_sort(first)
    merge_sort(second)
    i, j, k = 0, 0, 0
    len1, len2 = len(first), len(second)
    while j < len1 and k < len2:
        if first[j] and second[k]:
            if first[j] > second[k]:
                list_[i] = first[j]
                j += 1
            else:
                list_[i] = second[k]
                k += 1
            i += 1
    while j < len1:
        list_[i] = first[j]
        j += 1
        i += 1
    while k < len2:
        list_[i] = second[k]
        k += 1
        i += 1


# функция генерации отсортированого списка с рандомных чисел
# принимает длину списка, нижнюю и верхнюю граници генерации случайних чисел
# возвращает список отсортированый по убыванию
def list_gen(len_, start, end):
    list_ = [randint(start, end) for _ in range(len_)]
    merge_sort(list_)
    return list_


@time
def main():
    list1 = list_gen(1000, 0, 100000)
    list2 = list_gen(1000, 0, 100000)
    print(list1)
    print(list2)
    print(merge(list1, list2))


main()
