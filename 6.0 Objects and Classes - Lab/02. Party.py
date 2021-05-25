class Party:
    def __init__(self):
        self.users = []

    def __str__(self):
        return f'Going: {", ".join(self.users)}\nTotal: {len(self.users)}' 


add_people = Party()
name = input()
while name != 'End':
    add_people.users.append(name)
    name = input()  

print(add_people)