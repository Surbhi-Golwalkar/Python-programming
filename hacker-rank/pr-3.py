# Task
# The provided code stub reads two integers, a and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division, a // b . The second line should contain the result of float division, a / b .

# No rounding or formatting is necessary.


a = int(input("enter"))
b = int(input("enter"))

# print("{}\n{}".format(a//b, a/b))
print(a//b,a/b,sep="\n")
# print(a//b)
# print(a/b)