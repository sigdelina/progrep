
# coding: utf-8

# In[55]:


import re
import os

with open('sentences.csv', 'w', encoding='utf-8') as file: 
    row = '%s\t%s\t%s\t%s\t%s\t%s\t%s\n'
    file.write(row % ('Path', 'Tag', 'Full sentence', 'Tagged mistake', 
                   'Corrected mistake', 'Correct/incorrect', 'Group'))
path = './data/exam2017_1'
for root, dirs, files in os.walk(path):
    for file in files:
        if ".ann" in file:
            print(root, dirs, file)
            final = os.path.join(root, file)
            with open(final, encoding="utf-8") as file:
                annot_txt = file.read()
          #  print(annot_txt)
            clean_text = annot_txt.splitlines()
            for line in clean_text:
              #  print(line)
                find_tag = re.search(r'T.*?Tense_choice.*?\D', line)
                if find_tag is not None:
                    reg_mistake = re.search(r'\s\d*?\s\d*?\s(\D+)', line, flags=re.DOTALL)
                    tag_mistake = reg_mistake.group(1)
                    position = clean_text.index(line)
                    print(tag_mistake)
                    print(position)
                    pos_for_wrong = position + 1
                    print(pos_for_wrong)
                    сorrection = clean_text[pos_for_wrong]
                    print(сorrection)
                    reg_correct = re.search(r'#.*T\d*?\s(\D+)',  сorrection, flags=re.DOTALL)
                    if reg_correct is None:
                        correct_mistake = ' - '
                    else:
                        correct_mistake = reg_correct.group(1)
                    print(correct_mistake)
                    with open('sentences.csv', 'a', encoding='utf-8') as f:
                        row = '%s\tTense_choice\t%s\t%s\t%s\n'
                        f.write(row % (final, 'gt', tag_mistake, correct_mistake))
                        
                    
                    
            

