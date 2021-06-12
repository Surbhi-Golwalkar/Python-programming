num = int(input("enter number:"))
prime = True

for i in range(2,num):
    if(num%i == 0):
        prime = False
        break

if (num==0 or num==1):
    print("This is not a prime number")
elif prime:
    print("This number is Prime")
else:
    print("This number is not prime")