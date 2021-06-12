class recharge:
    def company(self):
        
        a = int(input("enter company:"))
        if(company =="Jio"):
            print("1gb/day = 199/-")
            print("2gb/day = 399/-")
            print("3gb/day = 699/-")

        if(company =="Idea"):
            print("1gb/day = 199/-")
            print("2gb/day = 399/-")
            print("3gb/day = 699/-")

        if(company =="Airtel"):
            print("1gb/day = 199/-")
            print("2gb/day = 399/-")
            print("3gb/day = 699/-")

        else:
            print("enter correct company")

class balance(recharge):
    acc = 400
    def getrecharge(self):
        plan = int(input("enter plan:"))
        if(plan<=acc):
            print("recharge successful")
        else:
            print("recharge unsuccessful")

c = recharge()
print(c.a)




