from re import finditer

pattern=r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
numbers = input()
results= finditer(pattern,numbers)

for result in results:
    print(result.group(0), end=' ')
