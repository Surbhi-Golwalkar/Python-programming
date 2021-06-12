#single inheritence
class itm:
    company = "pninfosys"
    
    def __init__(self):
        print("Hello MITS")

    def mits(self):
        print("Hello")

class mpct(itm):
    city = "gwalior"


m = mpct()
print(m.company)
print(m.city)
m.mits()