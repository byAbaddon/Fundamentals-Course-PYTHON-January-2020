import re

text = input()
word = input()

result = re.findall(rf'\b{word}\b', text, re.IGNORECASE)
print(len(result))
