catalog = {}

class Parking:
    def __init__(self, command, name, number ):
        self.command = command
        self.name = name
        self.number = number    
        self.catalog = catalog

    def registration(self):
        if self.name not in self.catalog:
            self.catalog[self.name] = self.number   
            return f'{self.name} registered {self.number} successfully'
        else:           
            return f'ERROR: already registered with plate number {self.number}'

    def unregister (self):
        if self.name in self.catalog:
            del self.catalog[self.name]       
            return f'{self.name} unregistered successfully'
        else:           
            return f'ERROR: user {self.name} not found'
    
    def __str__(self):
       collection = [] 
       for k,v in self.catalog.items():
            collection.append(f'{k} => {v}')
       return '\n'.join(collection) 


for _ in range(int(input())):
    data  = input().split()
    command, name  = data[0], data[1]
    number = data[2] if len(data) == 3  else None
        
    park = Parking(command, name, number)
    if command == 'register': 
        print(park.registration())
    else:
        print(park.unregister())

print(park)

 