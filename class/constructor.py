class Employee:
    company = "pninfosys"

#     def  __init__(self):
#         print("Hello Gwalior")

    def  __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getDetails(self):
        print(f"The name of the employee is {self.name}") 
        print(f"The name of the employee is {self.salary}")     
        


# rohit = Employee()  
rohit = Employee("raj","rohit")
rohit.getDetails()