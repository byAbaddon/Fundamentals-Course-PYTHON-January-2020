collection = list(reversed(input().split(', ')))

if collection[0] == 'wolf': 
  print('Please go away and stop eating my sheep')
else:
  index = collection.index("wolf")
  print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')


  # wolf, sheep, sheep, sheep, sheep, sheep
  # sheep, sheep, wolf, sheep, sheep, sheep