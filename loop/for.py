

course = ["html","python","php","laravel"]
for c in course:
    print(c)

#i=0
# while i<len(course):
#     print(course[i])
#     i=i+1



# Range function in python is used to generate a sequence of nu,bers. We can also specify the start, stop and step size.

i=0
for i in range(8):      #range(1,8)           #last number doesn't get printed
    print(i)

for i in range(1,8,2):  #range(1,8,step size)(1 no.s are skipped)
    print(i)

adj = ["red","big","tasty"]             #loop in loop
fruits=["apple","mango","banana"]
vegetables=["potato","brinjal","peas"]

for x in adj:
    for y in fruits:
        for z in vegetables:
            print(x,y,z)
        
