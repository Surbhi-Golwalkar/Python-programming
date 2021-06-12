a={
    "name" : "surbhi",
    2 : [1,3,2,5,4,4,3,6],
    4 : ("abc","xyz"),
    "education": {"surbhi" : "B.tech"}
}
#print(type("education"))   #this shows the type is string bcz particular edu.. is a string 
print(type(a["education"])) #if you want to know the type alaways write it like this
print(type(a[4]))
print(a[2])
a[2] =[10,13,60,98,60,50]
print(a[2])
print (type(a[2]))
print (a)
print("value at third place =", a[2][2])
