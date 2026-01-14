class Employee:
    company_name = "TCS"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
emp1 = Employee("amrit","150000")
emp2 = Employee("amrit rajput","150000")
print(emp1.company_name)
print(emp2.company_name)
Employee.company_name = "apple"
print(emp1.company_name)
print(emp2.company_name)
emp1.company_name = "meta"
print(emp1.company_name)
print(emp2.company_name)


