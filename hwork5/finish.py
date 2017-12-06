print("Вариант 2")
word = input("Add word: ")
word_list = [] 
word_list.append(word)
while word != "":
    word = input("Add more: ")
    word_list.append(word)
with open ("text1.txt", "w", encoding="utf-8") as file:
    for word in word_list:
        if len(word) > 5:
            with open ("text1.txt", "a", encoding = "utf-8") as file:
                file.write(word + "\n")

