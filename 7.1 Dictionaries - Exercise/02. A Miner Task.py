count_dict = {}

while True:
    key = input()
    if key == 'stop':
        break
    val = int(input())
    if key not in count_dict:
        count_dict[key] = 0
    count_dict[key] += val
    
for k,v in count_dict.items():
    if k != ' ':
        print(k, '->', v)