items_dict = {}

while True:
    try:
        product, price, quantity = input().split()
        if product not in items_dict:
            items_dict[product] = {'price': 0.0 , 'quantity': 0}
        items_dict[product]['price'] = float(price)
        items_dict[product]['quantity'] += int(quantity)
    except:
        break

for k,v in items_dict.items():
    print(k, '->', f"{v['quantity'] * v['price']:.2f}")

