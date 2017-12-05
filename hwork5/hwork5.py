print ("Вариант 2")
word = str(input("Введите слово: "))
while len(word) > 0:
    more_word = str(input("Введите слово: "))
else:
    with open("text1.txt", "w", encoding = "utf-8-sig") as f:
        word = input()
        while word != "":
            if len(word) > 5:
                f.write("\n")
                f.write(word)
            word = input()
with open("text1.txt", encoding = "utf-8") as final_file:
    print(final_file.read().strip())
    
