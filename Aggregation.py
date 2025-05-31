class Employee():
    def __init__(self, name):
        self.name = name
    def show_detail(self):
        print(f"Employee Name: {self.name}")

class Department():

    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

    def show_department(self):
        print(f"Department {self.dept_name}")
        self.employee.show_detail()

emp1 = Employee("Ali")
emp2 = Employee("Noman")
dept1 = Department("IT", emp1)
dept2 = Department("IT", emp2)

dept1.show_department()
dept2.show_department()