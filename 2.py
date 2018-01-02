c = input("Введите градусы по Цельсию:")
f = 0
k = 0
if c == '':
    print("no degree(")
else:
    c = int(c)
    f = float(c*(9/5) + 32)
    k = c*1 + 273,15
    print("Градусы по Фаренгейту:", f)
    print("Градусы по Кельвину:", k)
