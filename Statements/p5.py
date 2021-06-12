print("Welcome to our restuarant..!")
a=input("enter the name\n : ")
print("Choose anything from menu",a)
Menu ={
    "Noodles":"200/-",
    "Burger":"150/-",
    "Pizza":"300/-",
    "cake":"300/-",
    "ice cream":"80",
    "milkshake":"150/-"
}
food = input("Enter :\n")
price = input("Enter :\n")

if(food=="noodles" and price=="200"):
    print("your order for noodles has been ordered")

elif(food=="Burger" and price=="150"):
    print("your order for Burger has been ordered")

elif(food=="Pizza" and price=="300"):
    print("your order for Pizza has been ordered")

elif(food=="cake" and price=="300"):
    print("your order for cake has been ordered")

elif(food=="ice cream" and price=="80"):
    print("your order for ice cream has been ordered")

elif(food=="milkshake" and price=="150"):
    print("your order for milkshake has been ordered")
else:
    print("please enter from menu")