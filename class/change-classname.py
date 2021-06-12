class Employee:
    company  = "pninfosys"
    salary = 100


rahul = Employee()
rohit = Employee()

print(rahul.company)
print(rohit.company)
Employee.salary=1000
Employee.company ="google"
print(rahul.salary)
print(rohit.company)