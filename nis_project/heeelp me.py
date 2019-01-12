
# coding: utf-8

# In[82]:


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
            print(root, dirs, file)
            final_ann = os.path.join(root, file) # полный путь к файлу
            with open(final_ann, encoding="utf-8") as file:
                annot_txt = file.read()
          #  print(annot_txt)
            clean_text = annot_txt.splitlines() # список строк
            for line in clean_text: # обход строк в списке
              #  print(line)
                find_tag = re.search(r'T.*?Tense_choice.*?\D', line) # для строки с нужным тегом
                if find_tag is not None:
                    tag_mistake = re.search(r'T\d.*\d\s(\D+)', line, flags=re.DOTALL) # ошибка
                    mistake = tag_mistake.group(1)
                    position = clean_text.index(line)
                   # print(tag_mistake)
                   # print(position)
                    pos_for_wrong = position + 1 # позиция строки с ошибкой
                   # print(pos_for_wrong)
                    сorrection = clean_text[pos_for_wrong]
                    #print(сorrection)
                    tag_correct = re.search(r'#.*T\d.*\s(\D+)',  сorrection, flags=re.DOTALL)
                    if tag_correct is None:
                        correct = ' - '
                    else:
                        correct = tag_correct.group(1)
                   # print(correct)
                   # tag_place = re.search(r'\s(\d*?)\s(\d*?)\s', line, flags=re.DOTALL)
                   # tag_start = tag_place.group(1)
                   # tag_end = tag_place.group(2)
                   # print(tag_start, '\n', tag_end)
                   # text_file = filename[0:-3] + 'txt'
                   # final_text = os.path.join(root, text_file)
                   # with open(final_text, encoding="utf-8") as ftxt:
                   #     clear_text = ftxt.read()
                   # clean = clear_text.replace('\n','')
                    
                    #вот здесь нужно это предложение вытащить из файла и чет я запуталась
                    
                    #text_string = list(clean.replace(' ', ''))
                   # print(text_string)
                # пополенение таблицы
                    with open('sentences.csv', 'a', encoding='utf-8') as f:
                        row = '%s\tTense_choice\t%s\t%s\t%s\t%s\t%s\n'
                        f.write(row % (final_ann, 'gt', mistake, correct, 'h', 't'))
                        
                    
                    
            

