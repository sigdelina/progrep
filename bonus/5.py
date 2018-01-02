letters = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxZz'
word = str(input("add word or phrase:"))
if word == '':
    print("no word((((")
else:
    for char in letters:
        word = word.replace(char, char + 'aig')
    print(word)
