#WE ALSO CALLED THIS ENCAPS


class Employee():
    def __init__(self,name,salary, ssn):
        self.name = name        #public
        self._salary = salary   #protected
        self.__ssn = ssn        #private

emp1 = Employee("Noman",12000, "121")

print(f"Employee Name: {emp1.name}")
print(f"Employee Salary: {emp1._salary}")

try:
    print(f"private SSN : {emp1.ssn}")
except AttributeError as e:
    print("Private SSN cannot access directly", e)

#but we can also get private variable using mangling method:
print(f"Private SSN # : {emp1._Employee__ssn}")