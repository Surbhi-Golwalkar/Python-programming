class  Employee:
    company = "google"
    def getSalary(self, signature):  #automatic pass parameter
        print("Salary is 100k")
        print(f"Salary is {self.salary}")
        print(f"Salary is this employee working in {self.company} is {self.salary} \n{signature}")
rohit = Employee()
rohit.salary =1000
#rohit.getSalary("Thanks!")  #Employee.getsalary(rohit)
rohit.getSalary("Thanks!")