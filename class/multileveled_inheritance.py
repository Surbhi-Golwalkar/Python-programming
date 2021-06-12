#single parent(base) and multiple child(derived)
class Person:
    country = "india"

    def takeBreath(self):
        print("I am breathing.....")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print("salary 10000")

    def takeBreath(self):
        print("I am an employee so i am Luckily Breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print("No salary to programmer")

    def takeBreath(self):
        print("I am an employee so i am Luckily Breathing...")

# p = Person()
# p.takeBreath()
# e = Employee()
pr = Programmer()
pr.takeBreath()



