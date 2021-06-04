#-----------------------------------------------------(1)---------------60pts  WTF????
from re import findall, sub

text = input()
title = findall(r'(?<=<title>).*(?=<\/title>)', text)[0]

body_content = findall(r'<body>.*<\/body>', text)[0]
content = findall(r'>([^<>]*)<', body_content)

just_content = ''
for word in content:
    word = word.replace('\\n',' ')
    just_content += word  + ' '

just_content = sub(r'[\s]+', ' ' ,just_content)

print(f'Title: {title.strip()}')
print(f'Content: {just_content.strip()}')

# footer = findall(r'(?<=<footer>).*(?=<\/footer>)', text)
# if len(footer) > 0:
#     print('Footer:', footer[0].strip()) 


#-------------------------------------------------------(2)-------------60 pts   TODO
# import re

# text = input()

# regex_full_text = r'>([^<>?]*)<'
# text = re.sub('\r?\n', '',text)

# get_text = re.findall(regex_full_text, text)
# filter_text = list(filter(lambda x: x != '\\n' and x != '', get_text)) 
# collection = ''

# print(f'Title: {filter_text.pop(0)}')
# for el in filter_text:
#     el = el.replace('\\n' , '')
#     collection += el + ' '

# print('Content:',collection)










