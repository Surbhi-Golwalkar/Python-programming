# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print (i)^2

#METHOD 1
n = int(input())

for i in range(n):
    print(i * i)
    n+=1

#METHOD2

n=int(input("ENTER :"))

for i in range(0,n): 
    i= i**2 
    print(i)

#METHOD 3

n = int(input("ENTER :"))
counter = 0

while (counter < n):
    print (counter**2)
    counter = counter + 1
