import os
os.system('cls' if os.name == 'nt' else 'clear')

gifts_list = list(input().split(' '))

while True:
   
    current  = input().split(' ')

    if len(current) == 2:
        com, gift = current[0], current[1]
    else:
        com, gift, index  = current[0], current[1], int(current[2])
    
    if com == 'No':
        break

    elif com == 'OutOfStock':
        gifts_list = list(map(lambda x: None if x == gift  else x , gifts_list ))
    elif com == 'Required':
        if len(gifts_list) -1 >= index and index >= 0:
           gifts_list[index] = gift
          
    elif com == 'JustInCase':
        gifts_list[-1] = gift
           

print( *filter(lambda x: x != None ,gifts_list))