import re

def make_file(wiki_name):
    file = open(wiki_name, encoding='utf-8')
    file = file.read()
    return file

def replace(file):
    rep = re.sub(r'(В[и́и]кинг)([^лтвудс][^у][^д])', r'Бурундук\2', file)
    words = re.sub(r'(викинг)([^ёйцукенгшщзхъфывапролджэячсмитьбю]|[ауеи][^ёйцукенгшщзхъфывапролджэячсмитьбю]|[оа][мхв][^ыао])', r'бурундук\2', rep)
    return words

def rewrite(words):
    with open("new-file.txt", "w", encoding="utf-8") as n_file:
        n_file = n_file.write(str(words))
    return n_file

def main():
    wiki_name = "Викинги — Википедия.html"
    file = make_file(wiki_name)
    replace_t = replace(file)
    rewrite_t = rewrite(replace_t)
    print("Замена \"викинг\" на \"бурундук\" оусществлена")
    
main()
