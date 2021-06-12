class Employee:
    company = "pninfosys"
    salary = 5600
    salarybonus = 400

    @property
    def totalsalary(self):
        return self.salary + self.salarybonus


    # def totalsalary(self):
    #     return self.salary+ self.salarybonus


    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus = val - self.salary


e = Employee()
print(e.totalsalary())
e.totalsalary = 6500
print(e.salary)
print(e.salarybonus) 