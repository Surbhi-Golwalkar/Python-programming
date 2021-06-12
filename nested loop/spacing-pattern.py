#METHOD 1
rows = 6

for row in range(1,rows):
    num = 1

    for j in range(rows,0,-1):
        if j>row:
            print(" ", end='')
        
        else:
            print("*", end='')
            num +=1

    print("")


#METHOD 2
n=4
for i in range(5):
    print((n-i) * " " + i * '*')