num = int(input())
result = ''

if num <= 14:
  result = 'drink toddy'
elif num > 14 and num <= 18:
  result = 'drink coke'
elif num > 18 and num <= 21:
  result = 'drink beer'
elif num > 21:
  result = 'drink whisky'

print(result)       