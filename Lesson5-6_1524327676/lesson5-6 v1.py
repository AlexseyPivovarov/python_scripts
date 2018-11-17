from random import randint
main = [randint(11, 100000) for _ in range(100)]
print("100 рандомных чисел:", main)

list1 = [i for i in main if i % 10 == 1]
print("Числа с единицей вконце:", list1)

list2 = [i for i in main if (
        sum(int(a) for a in str(i)[:len(str(i)) // 2]) ==
        sum(int(b) for b in str(i)[:-((len(str(i)) // 2) + 1):-1])
)]
print("Счастливые числа:", list2)

list3 = [i for i in main if sum(0 if str(i)[n] == str(i)[-(n + 1)] else 1 for n in range(len(str(i)) // 2)) == 0]
print("Полиндромы:", list3)

