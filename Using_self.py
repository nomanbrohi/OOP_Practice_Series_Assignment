class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f'Student Name: {self.name}')
        print(f'Marks: {self.marks}')

std1 = Student("noman", 72)
std1.display()