import re

data = input()
regex = r"\d{2}/[A-Z]{1}[a-z]{2}/\d{4}|\d{2}-[A-Z]{1}[a-z]{2}-\d{4}|\d{2}\.[A-Z]{1}[a-z]{2}\.\d{4}"
matches = re.findall(regex, data)

for d in matches:
    print(f'Day: {d[0:2]}, Month: {d[3:6]}, Year: {d[-4:]}') 