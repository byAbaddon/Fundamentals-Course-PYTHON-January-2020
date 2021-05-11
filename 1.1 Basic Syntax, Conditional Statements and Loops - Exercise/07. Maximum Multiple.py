div ,num = int(input()), int(input())

for i in range( num, 0, -1 ):
 if num % div != 0:
    num -= 1   
 else:
   print(num)
   break