import sys
n = int(input())
start = n
load = 0
bar = []

if n == 100:
    bar = ['%'] * 10
    print('100% Complete!')
    print('[' + ''.join(bar) +  ']')
    sys.exit()

while n > 0:
    n -= 10
    bar.insert(load,'%')
    load += 1

for _ in range(10 - load):
    bar.append('.')


print(str(start) + '%', '[' + ''.join(bar) +  ']')  
print('Still loading...')    

