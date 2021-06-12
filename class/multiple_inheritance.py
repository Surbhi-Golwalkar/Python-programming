#multiple base(parent) class and single derived(child) class

class employee:
    company = "pninfosys"
    code = 120

class freelancer:
    company = "google"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class programmer(employee,freelancer):
    name ="vikas"

p = programmer()
p.upgradeLevel()
print(p.level)
print(p.company)