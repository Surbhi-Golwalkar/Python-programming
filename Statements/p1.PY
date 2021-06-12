#user = "surbhi"
#password = 1233
#user ="vikas" #admin
#password=12345
#user:itm #(college)
#password:123

user = input("Enter username :\n")
password = input("Enter password :\n")

if(user=="surbhi" and password=="1233"):
    print("surbhi dashboard")

elif(user=="vikas" and password=="12345"):
    print("vikas dashboard")

elif(user=="itm" and password=="123"):
    print("college dashboard")

else:
    print("no login")