#program to find leap year or not year = int(input("Enter the year :"))
year = int(input("ENTER :"))
if(year%4==0  and year%100!=0 or year%400==0):
    print("leap year")

else:
    print("not a leap year")



# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

# def is_leap(year):
#     return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
#     leap = False
    
#     return leap

# year = int(input("enter"))
# print(is_leap(year))    