number = int(input())
first = 1

while True:
    year = str(number)
    
    if len(set(year)) == len(year) and first != 1:
      print(year)
      break

    number += 1
    first += 1
