num= int(input("Enter number:"))

print("Mult. table of:",num)
for i in range(1,11):
    print(str(num) + "x"+str(i) + "=" + str(num*i))  #simple format
   
    #print(f{num}x{i}={num*1})  #f-strings
    print(f"{num}x{i}={num*i}")