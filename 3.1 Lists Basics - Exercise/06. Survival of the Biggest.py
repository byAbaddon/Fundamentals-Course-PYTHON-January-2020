string = list(map(int, input().split(' ')))
n = int(input())
result = []
count = n

for i in range(0, len(string)):
    if string[i] > n:
        result.append(string[i])
    else:    
        count -= 1

if count > 0:        
    print(result[0 : count * -1])
else:
    print(result)