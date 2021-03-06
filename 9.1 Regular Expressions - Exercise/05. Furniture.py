from re import finditer

regex = r'^>>(?P<item>[A-Za-z]*)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)$'
furnitures = []
total_sum = 0 

while True:
    text = input()
    if text == 'Purchase':
        break
    match = finditer(regex, text)
    for element in match:
        furnitures.append(element.group('item'))
        total_sum += float(element.group('price')) * int(element.group('quantity'))

print('Bought furniture:')
for el in furnitures:
    print(el)
print(f'Total money spend: {total_sum:.2f}')