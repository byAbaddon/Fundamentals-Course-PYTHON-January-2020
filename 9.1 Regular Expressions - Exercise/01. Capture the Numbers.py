from re import findall

collection = ''

while True:
    data = input()
    if data == '':
        break
    collection += data

result = findall(r'\d+', collection)
print(' '.join(result))  

