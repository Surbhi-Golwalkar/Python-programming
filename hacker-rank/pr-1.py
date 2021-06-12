# Task
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird


#METHOD 1

n = int(input("enter :"))
if (n%2!=0):
    print("Weird")
    
elif (n%2==0 and 2<=n<=5):
    print("Not Weird")
    
elif (n%2==0 and 6<=n<=20):
    print("Weird")
    
else:
    print("Not Weird")




#METHOD 2
n = int(input("enter :"))

if n%2==0 and (n in range(2,6) or n>20 ):
    print ("Not")
else:
    print ("Weird")