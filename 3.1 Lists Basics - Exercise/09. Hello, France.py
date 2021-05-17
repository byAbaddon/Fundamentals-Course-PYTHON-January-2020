coll_list = input().split('|')
budget = float(input())
subtotal_sum = []

catalog = {'Clothes' : 50.00, 'Shoes' : 35.00, 'Accessories' : 20.50 }

while len(coll_list) > 0:
    current = coll_list.pop(0).split('->')
    item, price = current[0], float(current[1])

    if item in catalog.keys() and catalog[item] >= price and budget >= price:
        budget -= price
        subtotal_sum.append(price * 1.40)


profit = sum(subtotal_sum) - (sum(subtotal_sum) / 1.4)

print( *[f'{x:.2f}' for x in subtotal_sum]) 
print('Profit:', f'{profit:.2f}')

total_sum = sum(subtotal_sum) + budget
if total_sum >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
  
