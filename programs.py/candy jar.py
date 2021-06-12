# There is a JAR full of Candies for sale at a mail counter. JAR has capacity N, that is JAR can contain maximum N candles when JAR is full.
# At any point of time, JAR can have M number of candidates where M<=N. Candies are served to the customers. JAR is never remaining empty as when last k candies are left, JAR is refilled with new Candies in such as way that JAR get full.

# Write the code to implement above scenario. Display JAR at Counter with available number of candies.

# Input should be number of candies one customer orders at point of time. Update the JAR after every purchase and display JAR at Counter.

# Output should give number of Candies sold and udpated number of Candies in JAR. If input is more than number of Candies in JAR , return : "INVALID INPUT".

# Given,
# N = 10, where N is NUMBER OF CANDIES AVAILABLE
# k < = 5, where k is number of minimum Candies that must be inside JAR ever.

# Constraints

# N = 10 , k < =5

# Test Case 1

# Input :
# 3

# Output :
# NUMBER OF CANDIES SOLD: 3
# NUMBER OF CANDIES AVAILABLE: 7

# Test Case 2

# Input :
# 0

# Output :
# INVALID INPUT
# NUMBER OF CANDIES AVAILABLE: 10

#METHOD 1

n = int(input("Enter the no. of candies :"))
total=10

if n in range(1,6):
    print("NUMBER OF CANDIES SOLD :",n)
    print("NUMBER OF CANDIES AVAILABLE :",total-n)

else:
    print("INVALID INPUT")
    print("NO. OF CANDIES LEFT:",total)


#METHOD 2

i = int(input("Enter no. of candies :"))
n = 10
k = 5

if(i >n):
       print("INVALID INPUT")
       print("NUMBER OF CANDIES AVAILABLE:", end="")
       print(n)
elif(i <= 0):
       print("INVALID INPUT")
       print("NUMBER OF CANDIES AVAILABLE:", end="")
       print(n)

else:
      print("NUMBER OF CANDIES SOLD:", end="")
      print(i)
      print("NUMBER OF CANDIES AVAILABLE:", end="")
      print(n-i)