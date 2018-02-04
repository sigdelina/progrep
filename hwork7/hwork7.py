def read_text(choose_name):
    word_dict = {}
    ch_name = []
    symbols = [".", ",", "!", "?", "\"", " - ", "...", ":", ";", "(", ")", "\n", "1", "2", "3", "4", "5",]
    with open ("Pride_and_Prejudice.txt", "r", encoding = "utf-8") as file:
        for line in file:
            for char in symbols:
                line = line.replace(char, "")
                line = line.lower()
            word = line.split(" ")
    return word

def freq_word(word):
    word_dict = {}
    for words in word:
        if len(words) >= 4:
            if words[-4:] == "ness":
                if words in word_dict:
                    word_dict[words] += 1
                else:
                    word_dict[words] = 1
    print("Количество слов с -ness в тексте: ", len(word_dict))
    return word_dict

from operator import itemgetter

def max_word(word_dict):
    wordness = []
    wordness = sorted(word_dict.items(), key=itemgetter(1))
    wordness = list(map(str, wordness))
    print("Самвую высокую частоту имееть слово: (печатает и слово и его частоту))", wordness[-1:])

