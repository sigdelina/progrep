print ("Вариант 2")
word = input("Add word: ")
word_list = []
word_list.append(word)
while word != "":
    word = input("Add word: ")
    word_list.append(word)
with open("text1.txt", "w", encoding = "utf-8") as f:
    for word in word_list:
        if len(word) > 5:
            f.write("\n")
            f.write(word)
with open("text1.txt", encoding = "utf-8") as final_file:
    print(final_file.read().strip())
    
