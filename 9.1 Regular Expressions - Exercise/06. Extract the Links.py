from re import finditer
pattern=r'\bwww\.[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*(\.[a-z]+)+\b'

while True:
    command = input()
    if command == '':
        break

    for email in finditer(pattern,command):
        print(email[0])
    
    