arr = input().split()
search_products = input().split()
products = {}

for i in range(0, len(arr), 2):
    products[arr[i]] = int(arr[i + 1]) 


for key in search_products:
    if key in products:
        print(f'We have {products[key]} of {key} left')
    else:
        print(f'Sorry, we don\'t have {key}')    