print("2 вариант")
with open("Ozhegov.txt", "r", encoding = "utf-8")as file:
    for line in file:
        word = line.split("|")
        l = word[0].split(" ")
        if len(l[0]) > 20:
            print(line)
