obj = { 'coding' : 0,
        'CODING' : 0,   
        'movie' : 0,   
        'MOVIE' : 0,   
        'dog' : 0,   
        'DOG' : 0,   
        'cat' : 0,   
        'CAT' : 0,
        'count' : 0   
      }

entry = input()
counter = 0

while entry != 'END':
  obj['count'] +=1

  if entry in obj:
    if entry.isupper():
      obj[entry] += 2
      counter +=2
    else:  
      obj[entry] += 1
      counter +=1

  entry = input()


if counter > 5:
  print('You need extra sleep')
else:
  print(counter)



