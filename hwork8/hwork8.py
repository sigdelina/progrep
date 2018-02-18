import random

def nouns(): #здесь я практически полностью оперлась на конспект. Так как из задания непонятно, надо ли добавлять название файла сразу, я сделала так. ))))
    nouns = {}
    with open("csvslovar1.csv", "r", encoding="utf-8-sig") as file:
        fn = ''
        for lines in file:
            if lines == 'окно,открытое\n':
                continue
            if fn == '':
                desc, word = lines.strip("\n").split(',')
                nouns[desc] = [word]
        return nouns
            
def random_words(nouns):
    letters = ['абвгдеёжзийклмнопрстуфхцчшщьыыъэюя']
    print("Готовы ли Вы сыграть в игру и отгадать слово?")
    answer = input()
    if answer == "нет":
        exit(0)
    else:
        print("Необходимо отградать слово по подсказке.\nВам будет дана подсказка из часто употребляемого слова с существительным и многоточие,\nкоторое содержит столько точек, сколько букв в слове:\n")
        word = random.choice(list(nouns.keys()))
        desc = random.choice(nouns[word])        
        word1 = word
        for letters in word1:
           for char in letters:
                word1 = word1.replace(char, ".")
        helpword = desc + " " + word1
        print(helpword, "\n")
        return word
    
def poputka(word1):
        your_word = input("Введите слово: ",)
        if your_word != word1:
            print("\nЗагаданное слово '", word1, "'. Вы не угадали слово. Ждем Вас снова")
            exit(0)
        else:
            return  "\nВы угадали слово: " + your_word
        
filewords = nouns()
random = random_words(filewords)
trying = poputka(random)
print(trying)
