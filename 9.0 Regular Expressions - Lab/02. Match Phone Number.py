from re import findall

numbers = input()

regex = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
result = findall(regex, numbers)
print(', '.join(result))    