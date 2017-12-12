print("2 вариант")

print("задание 1")
with open("Ozhegov.txt", "r", encoding = "utf-8")as file:
    for line in file:
        word = line.split("|")
        l = word[0].split(" ")
        if len(l[0]) >= 20:
            print(line)

print("задание 2")
a = []
with open("Ozhegov.txt", "r", encoding = "utf-8")as file:
    for line in file:
        word = line.split("|")
        #line = line.replace("123456789\n ", "")
        if word[2] != "":
            a.append(line)
            #print(line) или print(word[2]) если нужно вывести строки с данными словами или сами слова
print(len(a))
            
print("задание 3")
