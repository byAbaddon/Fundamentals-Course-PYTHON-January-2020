import os
os.system('cls' if os.name == 'nt' else 'clear')

n = input()
collection = list()

for i in range(len(n)):
  if  n[i].isupper():
     collection.append(i)

print(collection)