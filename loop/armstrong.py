n=int(input("enter no."))
sum=0
# count=0

# i = n
# while i>0:
#     count= count+1
#     i=i//10
    

i = n
while i>0:
    remainder = i%10
    sum=sum+(remainder**3)
    i//=10

if n == sum:
    print("armstrong")

else:
    print("not a armstrong")

