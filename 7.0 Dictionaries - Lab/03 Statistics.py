d_dict = {}

while True:
    try:
        tokens = input().split(': ')
        if tokens[0] not in d_dict:
            d_dict[tokens[0]] = int(tokens[1])
        else:
            d_dict[tokens[0]] += int(tokens[1])    
    except:
        break

print('Products in stock:')
for k, v in d_dict.items():
    print('- {}: {}'.format(k,v))

print(f'Total Products: {len(d_dict)}')
print(f'Total Quantity: {sum(d_dict.values())}')    
