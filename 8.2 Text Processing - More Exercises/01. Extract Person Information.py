from re import findall

re_name = r'(?<=@)(.*)(?=\|)'
re_age =  r'(?<=#)(.*)(?=\*)'

for _ in   range(int(input())):
    text = input()
    find_name = findall(re_name, text)
    find_age =  findall(re_age, text)
    print(f'{find_name[0]} is {find_age[0]} years old.')
  