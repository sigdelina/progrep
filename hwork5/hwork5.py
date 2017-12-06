print ("Вариант 2")
word = input("Add word: ")
with open("text1.txt", "w", encoding = "utf-8-sig") as f:
    word = input("Add new word: ")
    while word != "":
        if len(word) > 5:
            f.write("\n")
            f.write(word)
        word = input("Add new word: ")
with open("text1.txt", encoding = "utf-8") as final_file:
    print(final_file.read().strip())
    
