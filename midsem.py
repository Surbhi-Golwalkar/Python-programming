x = int(input('Enter a number:'))
if(x%3 == 0 and x>0):
    raise Exception("Sorry, unacceptable input")