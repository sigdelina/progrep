#Бонусные задачи разрешали писать не функциями, поэтому они написаны не в них, а просто кодом.
a = input("Введите число: ")
number = 0
summa = 0
a_list = []
a_list.append(a)
if a == '':
    print("Нет числа")
else:
    while a != '':
        a = input("Введите число: ")
        a_list.append(a)
    del a_list[-1]
    a_list = list(map(int, a_list))
    for a in a_list:
        summa += a
        number += 1
    print("Минимальное число: ", min(a_list), ".", "Наибольшее число: " , max(a_list), ".", "Среднее арифмитическое: ", summa/number)
