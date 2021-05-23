num = list(map(int,input().split('.')))
a, b, c =  num[0], num[1], num[2]

c += 1
if c > 9:
    c = 0
    b +=  1
    if b > 9:
        b = 0
        a += 1
     
print(f'{a}.{b}.{c}')