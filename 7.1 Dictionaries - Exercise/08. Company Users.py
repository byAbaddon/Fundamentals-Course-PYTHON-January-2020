data = {}

while True:
    try:
        uni, num = input().split(' -> ')
        if uni not in data:
            data[uni] = []
        data[uni].append(num)
    except:
        break

sort_company = dict(sorted(data.items()))
for k, v in sort_company.items():
    print(k)
    uniq = sorted(set(v), key = v.index) 
    for num in uniq:
        print('--', num)