count_dict = {}

for char in input():
    if char not in count_dict:
        count_dict[char] = 0
    count_dict[char] += 1

for k,v in count_dict.items():
    if k != ' ':
        print(k, '->', v)