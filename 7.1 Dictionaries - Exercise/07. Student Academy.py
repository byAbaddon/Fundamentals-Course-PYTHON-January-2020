catalog = {}

class StudentAcademy:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.catalog = catalog

    def add_student(self):
        if self.name not in self.catalog:
            self.catalog[self.name] = [] 
        self.catalog[self.name].append(self.grade)

    def __str__(self):
        data = []
        avg = {}
        for k ,v in catalog.items():
             avg[k] = sum(v) / float(len(v))

        filter_students = dict((filter( lambda x: x[1] >= 4.50, avg.items())))
        sort_students = dict(sorted(filter_students.items(), key=lambda x: (-x[1], x[1] ))) 
    
        for k,v in sort_students.items():
            data.append(f'{k} -> {v:.2f}')
        return  '\n'.join(data)       


for _ in range(int(input())):
    user_name = input()
    grade = float(input()) 
    info = StudentAcademy(user_name, grade)
    info.add_student()
  
print(info)
        
