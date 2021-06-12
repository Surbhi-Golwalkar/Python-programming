# Dictionaries are used to store data value in  Key : Value pairs
#It is a collection of key value pairs

a = {
    "name":"pninfosys gwalior", # don't forget that last comma ever otherwise other dictionaries cant be printed
    "name 1": "pnoinfosys""pninfosys", #here comma will give us error so they can't be used
    "college": "M.I.T.S",

    # "college":"I.T.M", #Duplicates aren't allowed

    "Mark" : [1,2,3,4,5],           #list
    "b" : ('ram','MCA'),            #tuple
    "education" : {'ram':'MCA'},    #dictionary

}
print(a)
print(type(a))
print(type(a["Mark"]))
print(type(a["b"]))
print(type(a["education"]))
print(type(a["college"]))
print(a['education']['ram'])


