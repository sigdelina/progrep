#некоторые названия функций взяты из примера
print("Программа должна генерировать стихотворение из грамматически правильных, но бессмысленных предложений с соблюдением метрической схемы и отсутсвием рифмы - трехстопный амфибрахиль")
print("")
import random

def verb_plur():
    plural_verbs = []
    with open ("verb_plur.txt", "r",  encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = plural_verbs.extend(words)
    return random.choice(plural_verbs)

#думаю, что вполне можно сократить эту фнкцию, и все последующие путем объединения строчки со split и строчкой с добавлением в список, но так как в задании было написано, что хорошая функция - такая функция, где строчек <= 6, а здесь их ровно 6 штук, оставляю так, потому что нагляднее.

def verb_sg_m():
    sg_verbs_m = []
    with open ("verb_sg_m.txt", "r",  encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = sg_verbs_m.extend(words)
    return random.choice(sg_verbs_m)

def verb_sg_n():
    sg_verbs_n = []
    with open ("verb_sg_n.txt", "r",  encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = sg_verbs_n.extend(words)
    return random.choice (sg_verbs_n)

def verb_sg_f():
    sg_verbs_f = []
    with open ("verb_sg_f.txt", "r",  encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = sg_verbs_f.extend(words)
    return random.choice (sg_verbs_f)

def verb_for_phrase_f():
    sg_v_f_p = []
    with open ("verb_for_phrase_f.txt", "r",  encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = sg_v_f_p.extend(words)
    return random.choice( sg_v_f_p)

def verb_for_phrase_m():
    sg_v_m_p = []
    with open ("verb_for_phrase_m.txt", "r",  encoding = "utf-8") as file:
        for line in file:
            words = line.split("|")
            words = sg_v_m_p.extend(words)
    return random.choice(sg_v_m_p)

def verb_for_phrase_n():
    sg_v_n_p = []
    with open ("verb_for_phrase_n.txt", "r",  encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = sg_v_n_p.extend(words)
    return random.choice(sg_v_n_p)

def verb_for_phrase_pl():
    pl_v_p = []
    with open ("verb_for_phrase_pl.txt", "r",  encoding = "utf-8") as file:
        for line in file:
            words = line.split("|")
            words = pl_v_p.extend(words)
    return random.choice(pl_v_p)

def infinitiv():
    inf_f_pl =[]
    with open ("infinitiv.txt", "r",  encoding = "utf-8") as file:
        for line in file:
            words = line.split("|")
            words = inf_f_pl.extend(words)
    return random.choice(inf_f_pl)

def noun_f(): 
    sg_nouns_f = []
    with open ("noun_f.txt", "r",  encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = sg_nouns_f.extend(words)
    return random.choice(sg_nouns_f)

def noun_n():
    sg_nouns_n = []
    with open ("noun_n.txt", "r",  encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = sg_nouns_n.extend(words)
    return random.choice(sg_nouns_n)

def noun_m():
    sg_nouns_m = []
    with open("noun_m.txt", "r", encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = sg_nouns_m.extend(words)
    return random.choice(sg_nouns_m)

def noun_pl():
    plural_nouns = []
    with open("nouns_plur.txt", "r", encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = plural_nouns.extend(words)
    return random.choice(plural_nouns)

def noun_for_phrase_f():
    nouns_f = []
    with open("noun_for_phrase_f.txt", "r", encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = nouns_f.extend(words)
    return random.choice(nouns_f)

def noun_for_phrase_m():
    nouns_m = []
    with open("noun_for_phrase_m.txt", "r", encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = nouns_m.extend(words)
    return random.choice(nouns_m)

def noun_for_phrase_n():
    nouns_n = []
    with open("noun_for_phrase_n.txt", "r", encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = nouns_n.extend(words)
    return random.choice(nouns_n)

def punctuation():
    marks = []
    with open("punctuation.txt", "r", encoding = "utf-8") as file:
        for line in file:
            words = line.split(" ")
            words = marks.extend(words)
    return random.choice(marks)

def phrase_f():
    clitics = []
    with open("phrase_f.txt", "r", encoding = "utf-8") as file:
        for line in file:
            words = clitics.extend(line.split(" "))
    clitic = random.choice(clitics)
    return clitic + ' ' + noun_for_phrase_f()

def phrase_n():
    clitics = []
    with open("phrase_n.txt", "r", encoding = "utf-8") as file:
        for line in file:
            words = clitics.extend(line.split(" "))
    clitic = random.choice(clitics)
    return clitic + ' ' + noun_for_phrase_n()
    
def verse1():
    return  noun_pl() + ' ' + verb_plur() + ' ' + noun_pl() + punctuation()

def verse2():
    return noun_pl() + ' ' + verb_plur() + ' ' + noun_n() + punctuation()

def verse3():
    return noun_n() + ' ' + verb_sg_n() + ' ' + noun_n() + punctuation()

def verse4():
    return noun_n() + ' ' + verb_sg_n() + ' ' + noun_pl() + punctuation()

def verse5():
    return noun_m() + ' ' + verb_sg_m() + ' ' + noun_pl() + punctuation()

def verse6():
    return noun_m() + ' ' + verb_sg_m() + ' ' + noun_n() + punctuation()

def verse7():
    return noun_f() + ' ' + verb_sg_f() + ' ' + noun_n() + punctuation()

def verse8():
     return noun_f() + ' ' + verb_sg_f() + ' ' + noun_pl() + punctuation()

def verse9():
    return noun_f() + ' ' + verb_for_phrase_f() + ' ' + phrase_f() + punctuation()

def verse10():
    return noun_m() + ' ' + verb_for_phrase_m() + ' ' + noun_for_phrase_m() + punctuation()

def verse11():
    return noun_n() + ' ' + verb_for_phrase_n() + ' ' + phrase_n() + punctuation()

def verse12():
    return noun_pl() + ' ' + verb_for_phrase_pl() + ' ' + infinitiv() + punctuation()

def make_verse():
    verse = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    if verse == 1:
        return verse1()
    if verse == 2:
        return verse2()
    if verse == 3:
        return verse3()
    elif verse == 4:
        return verse4()
    elif verse == 5:
        return verse5()
    elif verse == 6:
        return verse6()
    elif verse == 7:
        return verse7()
    elif verse == 8:
        return verse8()
    elif verse == 9:
        return verse9()
    elif verse == 10:
        return verse10()
    elif verse == 11():
        return verse11
    else:
        return verse12()

for n in range(4):
    print(make_verse())
        
