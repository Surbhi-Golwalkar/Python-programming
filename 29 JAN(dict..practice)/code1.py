#program to get price of any course from options given in code, entered by user

course ={
    "php":"1000",
    "python":"2000",
    "Html":"1000",
    "Angular":"3000",
    "company":"1500"
}
print("option course",course.keys())
a=input("Enter the course :\n")

#print("The course fee is:",course[a])
#below line will not give an error if the key is not present in it
print("The course fee is:",course.get(a))
