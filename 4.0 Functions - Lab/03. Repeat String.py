import os
os.system('cls' if os.name == 'nt' else 'clear')

string = input()
num = int(input())

def repeater(st,re):
   return st * re

print(repeater(string, num))