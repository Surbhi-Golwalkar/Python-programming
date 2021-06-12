# n=int(input("Enter no. upto which you want to add:"))
# i=2
# while(i<=n): 
#     if (i%2==0):
#         print(i)
#     i=i+1

# i=2
# while(i<n):
#     print(i)
#     i=i+2

# i=int(input("Enter no. :"))
# sum=0
# while(i>0):
#     sum = sum+i%10
#     i=i//10
# print("Sum Of Digits =",sum)


i=int(input("Enter no. :"))
sum=0
while(i>0):
    sum = sum+(i%10 * i%10 )
    #  sum = sum+(i%10 * i%10 * i%10 )
    i=i//10
print("Sum Of square of Digits =",sum)
# print("Sum Of cube of Digits =",sum)
