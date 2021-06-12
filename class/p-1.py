class a:
    company = "pninfosys"

#     def  __init__(self):
#         print("Hello Gwalior")

    def  __init__(self, square, cube):
        self.square = square*9
        self.cube = cube*18

    def getDetails(self):
        print(f"The value of 9 square is : {self.square}") 
        print(f"The value of 9 cube is : {self.cube}")     
        


# rohit = Employee()  
b = a("9","9")
b.getDetails()