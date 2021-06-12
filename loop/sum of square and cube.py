n=int(input("Enter no. upto which you want to add:"))
sum=0
i=1
while(i<=n): 
    sum = sum + (i*i)
    #sum= sum+(i*i*i)
    i = i+1
print("Sum of square of no. is",sum)
#print("Sum of cube of no. is",sum)
