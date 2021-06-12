n=int(input("enter no."))
i=n
reverse = 0
while(n>0):
    remainder = n%10
    reverse = (reverse*10)+remainder
    n = n//10
if(i == reverse):
    print("no. is palindrome")
else:
    print("not a palindrome")