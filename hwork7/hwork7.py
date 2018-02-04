#2 вариант

def name():
    ch_file = input("Введите название файла: ")
    if ch_file == '':
        print("no name")
        exit(0)
    else:
        return ch_file
    
def read_text(ch_file):
    symbols = [".", ",", "!", "?", "\"", " - ", "...", ":", ";", "(", ")","\t", "\n", "1", "2", "3", "4", "5","6", "7", "8", "9", "0", "^", "{", "}", ">", "<", "/", "|", "%", "@", "#", "№", "$"]
    awords = []
    with open (ch_file, "r", encoding = "utf-8") as file:
        for line in file:
            for char in symbols:
                line = line.replace(char, "").lower()
            word = line.split()
            for words in word:
                awords.append(words)
    return awords

def freq_word(awords):
    word_dict = {}
    for words in awords:
        if len(words) > 4:
            if words[-4:] == "ness":
                if words in word_dict:
                    word_dict[words] += 1
                else:
                    word_dict[words] = 1
        else:
            print("слова с суффиксом -ness нет")
            exit(0)
    return word_dict

from operator import itemgetter

def max_word(word_dict):
    wordness = []
    wordness = sorted(word_dict.items(), key=itemgetter(1))
    return wordness[-1:]

ch_file = name()
words = read_text(ch_file)
word_dict = freq_word(words)
print("Количество слов с -ness в тексте: ", len(word_dict))
print("Самую высокую частоту имееть слово: (печатает и слово и его частоту))", max_word(word_dict))

