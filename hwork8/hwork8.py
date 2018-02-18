import random

def nouns(): #здесь я практически полностью оперлась на конспект
    nouns = {}
    with open("csvslovar1.csv", "r", encoding="utf-8-sig") as file:
        fn = ''
        for lines in file:
            if lines == 'word,desc\n':
                continue
            if fn == '':
                desc, word = lines.strip().split(',', maxsplit = 1)
                nouns[desc] = word
        return nouns
            
def random_words(nouns):
    letters = ['абвгдеёжзийклмнопрстуфхцчшщьыыъэюя']
    print("Готовы ли Вы сыграть в игру и отгадать слово?")
    answer = input()
    if answer == "нет":
        exit(0)
    else:
        print("Необходимо отградать слово по подсказке.\nВам будет дана подсказка из часто употребляющегося слова с существительным и многоточие,\nкоторое содержит столько точек, сколько букв в слове:\n")
        word = random.choice(list(nouns.keys()))
        word1 = word
        for letters in word1:
            for char in letters:
                word1 = word1.replace(char, ".")
        print(word1)
        helpword =  " " + word
        your_word = input("Введите слово: ")
        if your_word != word:
            print("Загаданное слово: ", word, "\nВы не угадали слово. Ждем Вас снова")
            exit(0)
        else:
            print("Вы угадали слово")
            return your_word

filewords = nouns()
random = random_words(filewords)
print(random)
