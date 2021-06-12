# print factorial (factorial of 5 =1X2X3X4X5)

num = int(input("enter number"))
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
print(f"The factorial of this {num} is {factorial}")