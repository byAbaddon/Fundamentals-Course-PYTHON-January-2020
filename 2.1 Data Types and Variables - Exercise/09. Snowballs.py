n = int(input())
collection = {}
snowball_value = 0

while n > 0:
   snowball_snow = int(input())
   snowball_time = int(input())
   snowball_quality  = int(input())
    
   snowball_value = int(snowball_snow / snowball_time) ** snowball_quality
   collection[snowball_value ] = f'{snowball_snow} : {snowball_time} = {snowball_value} ({snowball_quality})'
   
   n -= 1

for key, value in sorted(collection.items(), reverse=True):
   print(value)
   break