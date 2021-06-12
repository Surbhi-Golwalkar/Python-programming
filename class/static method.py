#here attributes can not be used
class Employee:
    company = "gwalior"

    @staticmethod
    def mits(name):
        print((f"hello {name}"))

a = Employee()
a.mits("Surbhi")