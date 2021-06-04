import re

name_list = { x : x if x == None else 0 for x in  input().split(', ')}
regex_char = r'(?P<char>[A-Za-z])'
regex_digit = r'(?P<digit>\d)'

while True:
    text = input()
    if text == 'end of race':
        break

    result_char = re.findall(regex_char,text)
    result_digit = re.findall(regex_digit,text)

    name = ''.join(result_char)
    sum_km = sum(map(int, (result_digit)))

    if name  in name_list:
        name_list[name] += sum_km


sort_name_list = dict(sorted(name_list.items(), key=lambda x: -x[1]))
index = 1

for key in sort_name_list:
    if index < 4:
        position = ['st', 'nd', 'rd']
        print(f'{index}{position[index - 1]} place: {key}')
    index += 1