arr = [int(input())  for x in range(3)]
total = arr[0] * arr[1] * arr[2]

if total < 0:
    print('negative')
elif total == 0:
    print('zero')
else:
    print('positive')        