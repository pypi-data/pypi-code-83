# Made by Snehashish Laskar
# Made on 5/5/2021
# This is a simple Pythogoreas theorum calculator!= 0

def calculate(a= 0, b=0, c=0):
    if c == 0 and a != 0 and b != 0:
        try:
            c = (a**2 + b**2)**(1/2)
            print( "a = {}\nb = {}\nc = {}\n".format(a, b, c))
        except:
            print("error")
    elif a == 0 and c != 0 and b != 0:
        a = (c**2 - b**2)**(1/2)
        print( "a = {}\nb = {}\nc = {}\n".format(a, b, c))
    elif b == 0 and a != 0 and c != 0:
        b = (c**2 - a**2)**(1/2)
        print( "a = {}\nb = {}\nc = {}\n".format(a, b, c))
    else:
        print("There is nothing to Calculate!!")