class Person():
    def __init__(self, name):
        self.name = name
        print(f"Person Created: {self.name}")
    
class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher teaches: {self.subject}")

t = Teacher("Noman", "programming")

# print(t.name,t.subject)