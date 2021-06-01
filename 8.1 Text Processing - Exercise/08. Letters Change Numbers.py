data = input().split()
alphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
total_sum = 0

for el in data:
    first_leter = el[0]
    last_leter = el[-1]
    number = int(el[1:-1])

    if first_leter.isupper():
        total_sum += number / alphabet[first_leter]
    else:
        total_sum += number * alphabet[first_leter.upper()]
    
    if last_leter.isupper():
        total_sum -=  alphabet[last_leter]
    else:
        total_sum +=  alphabet[last_leter.upper()]
    
print(f'{total_sum:.2f}')
