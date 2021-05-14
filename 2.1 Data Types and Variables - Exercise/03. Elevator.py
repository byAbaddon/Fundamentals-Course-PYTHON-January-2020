import os
os.system('cls' if os.name == 'nt' else 'clear')

people = int(input())
capacity = int(input())
counter = 0

while people > capacity:
  people -= capacity
  counter +=1   

if people > 0:
  counter +=1

print(counter)