keyword = {"break", "case", "continue", "default", "defer", "else", "for", 
"func", "goto", "if", "map", "range", "return", "struct", "type", "var"}

a = input("ENTER :")
if a in keyword:
    print(a + " is a keyword")
else:
    print(a + " is a not keyword")