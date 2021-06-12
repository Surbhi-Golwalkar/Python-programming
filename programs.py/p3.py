n = int(input( "enter nth term :"))
a=0
b=0

for i in range(1,n+1):
    if(i%2!=0):
        a=a+7
    else:
        b=b+6

if(n%2!=0):
    print('{} term of series is {}'.format(n,a-7))

else:
    print('{} term of series is {}'.format(n,b-6))