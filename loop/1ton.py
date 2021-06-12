#program to print 1 to n
n = int(input("enter number:"))
i=1
while(i<=n):
    print(i)
    i=i+1

#program to print n to 1
n = int(input("enter number:"))
while(n>=1):
    print(n)
    n=n-1

# #Program to print from 10 to 1.
i = 10
while(i>=1):
    print(i)
    i=i-1

# #program to find sum from 1 to n

n=int(input("Enter no. upto which you want to add:"))
sum=0
i=1
while(i<=n): #3(i<=3)(<1<=3)(sum=sum+i)(sum(1)=0+1) (i=i+1) (i(2)=1+i)
    sum=sum+i
    i = i+1
print("Sum is",sum)
