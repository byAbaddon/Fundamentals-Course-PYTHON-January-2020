emails = []

while True:
    try:
        line = input()
        sender, receiver, content = line.split()
        emails.append(f'{sender} says to {receiver}: {content}. Sent:')
    except:
        break


test = list(map(int, input().split(', ')))   

for i in range( len(emails)):
   if i not in test:       
        print(emails[i],'False')
   else:
       print(emails[i],'True')
