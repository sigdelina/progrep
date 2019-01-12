import re
import os

# создает таблицу
with open('sentences.csv', 'w', encoding='utf-8') as file: 
    row = '%s\t%s\t%s\t%s\t%s\t%s\t%s\n'
    file.write(row % ('Path', 'Tag', 'Full sentence', 'Tagged mistake', 
                   'Corrected mistake', 'Correct/incorrect', 'Group'))
path = './data/' # прописывает путь
# обходит дерево
for root, dirs, files in os.walk(path):
    for file in files:
        if ".ann" in file: # для файлов с нужным расширением
            filename = str(file)
         #   print(root, dirs, file)
            final_ann = os.path.join(root, file) # полный путь к файлу
            with open(final_ann, encoding="utf-8") as file:
                annot_txt = file.read()
          #  print(annot_txt)
            clean_text = annot_txt.splitlines() # список строк
            for i in range(len(clean_text)-1): # обход строк в списке
              #  print(line)
                find_tag = re.search(r'T.*?Tense_choice.*?', clean_text[i]) # для строки с нужным тегом
                if find_tag is not None:
                    tag_id = re.search(r'(T\d*?)\s', line)
                    identif = tag_id.group(1)
                    tag_id_path = os.path.join(final_ann[7:-4], identif)
                    print(tag_id_path)
                    tag_mistake = re.search(r'T\d.*\d\s(.*)', clean_text[i], flags=re.DOTALL) # ошибка
                    mistake = tag_mistake.group(1)
                    tag_correct = re.search(r'#.*T\d.*\s(.*)', clean_text[i+1], flags=re.DOTALL)
                    if tag_correct is None:
                        correct = ''
                    else:
                        correct = tag_correct.group(1)
                    tag_place = re.search(r'\s\d.*\d?\s', clean_text[i], flags=re.DOTALL)
                    position = tag_place.group()
                    pos1 = position.split()
                    print(pos1)
                    #tag_start = tag_place.group(1)
                    #tag_end = tag_place.group(2)
                # пополенение таблицы
                    with open('sentences.csv', 'a', encoding='utf-8') as f:
                        row = '%s\tTense_choice\t%s\t%s\t%s\t%s\t%s\n'
                        f.write(row % (tag_id_path, "th", mistake, correct, 'h', 't'))
