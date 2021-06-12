# A Washing Machine works on the principle of a Fuzzy system, 
# the weight of clothes put inside it for wash is uncertain.
#  But based on weight measured by sensors, it decides time and water 
#  levels which can be changed by menus given on the machine control 
#  area. For low Water level, time estimate is 25 minutes, where 
#  approximate weight is 2000 grams or any non-zero positive number 
#  below that. For Medium Water level, time estimated is 35minutes, 
#  where approximate weight is between 2001 grams and 4000 grams.
# For High Water level, time estimated is 45 Minutes, 
# where approximate weight is above 4000 grams. 
#  Assume the Capacity of the Machine is maximum 7000 grams. 
# Where the approximate weight is zero, the time estimate is 0 minutes.
# Write a function which takes numeric weight in the range [0,7000]
# as input and produces estimated time as output;
#  if input is more than 7000, then output is: “OVERLOADED!”, 
#  and for all other inputs, the output statement is “INVALID INPUT”. 
#  Input should be in the form of integer value – Output must have the 
#  following format – Time Estimated: Minutes

# Example 1
# Input Value
# 2000
# Output Value
# Time Estimated: 25 Minutes

n = int(input("Enter no."))
if n==0:
    print("Time Estimated : 0 Minutes")
elif n in range(1,2001):
    print("Time Estimated : 25 Minutes")
elif n in range(2001,4001):
    print("Time Estimated : 35 Minutes")
elif n in range(4001,7001):
    print("Time Estimated : 45 Minutes")
else:
    print("INVALID INPUT")