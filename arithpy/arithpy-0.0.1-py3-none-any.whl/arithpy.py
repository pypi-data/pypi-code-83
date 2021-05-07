"""
       ArithPy
  ******************
 ArithPy is a simple and easy to use python moduloe made for basic arithmetic operations. The main purpose of creating such python module is to help developers to do calculations quickly in their programs made made by two school going students Suresh Mishra and Sai Binayak Biswal.
"""
#beginning of the module
# BASIC ARITHMETIC OPERATIONS
def sumnum(x,y):
    # addition function
    return (x+y)

def diffnum(x,y):
    # substraction function
    return (x-y)

def prodnum(x,y):
    # multipliaction function
    return (x*y)

def dividenum(x,y):
    # division function
    if y == 0:
        print("ERROR: Division by Zero")
    else:
        return (x/y)

def fdividenum(x,y):
    # floor division function
    return (x//y)

def modulo(x,y):
    # modulus function
    return (x%y)

def expo(x,y):
    #exponent or power function 
    return (x**y)

def square(x):
    # square function
    return (x*x)

def squarert(x):
    # square root function
    return (x ** 0.5)

def cube(x):
    # cube function
    return (x*x*x)

def cubert(x):
    # cube root function
    return (x ** (1/3))

# TIME CONVERSION
def hrtomin(x):
    # hour to minute conversion function
    return (x*60)

def mintosec(x):
    # minute to second conversion function
    return (x*60)

def hrtosec(x):
    # hour to second conversion function
    return (x*3600)

def mintohr(x):
    # minute to hour conversion function
    return (x/60)

def sectohr(x):
    # second to hour conversion function
    return (x/3600)

def sectomin(x):
    # second to minute conversion function
    return (x/60)

def mintomsec(x):
    # minute to millisecond conversion function
    return (x*60000)

def msectomin(x):
    # millisecond to minute conversion function
    return (x/60000)

def sectomsec(x):
    # second to millisecond conversion function
    return (x*1000)

def msectosec(x):
    # millisecond to second conversion function
    return (x/1000)

# TEMPERATURE CONVERSION
def ctof(x):
    # celsius to farhenhiet conversion function
    return ((x*9/5)+32)

def ctok(x):
    # celsius to kelvin conversion function
    return (x+273.15)

def ftoc(x):
    # farhenheit to celsius conversion function
    return ((x-32)*5/9)

def ftok(x):
    # farhenheit to kelvin conversion function
    return ((x-32)*5/9+273.15)

def ktoc(x):
    # kelvin to celsius conversion function
    return (x-273.15)

def ktof(x):
    # kelvin to farhenheit conversion function
    return ((x-273.15)*9/5+32)

# MISSCELLENOUS
def pi():
    # pi constant
    return (3.14)

def sintrst(x,y,z):
    # simple interest function
    # x is principal
    # y is time
    # z is rate of interest
    return ((x*y*z)/100) 

# AREA OF SHAPES
def arrect(x,y):
    # Area of rectangle
    # x is length
    # y is width/breadth
    return (x*y)

def arsqr(x):
    # Area of square
    # x is the sides of square
    return (x*x)

def artrngl(x,y):
    # Area of triangle
    # x is the base
    # y is the height
    return ((1/2)*x*y)

def arcyl(x,y):
    # Area of Cylinder
    # x is the radius
    # h is the height
    return (2*3.14*x*y)

def arcon(x,y):
    # Area of Cone
    # x is the radius
    # y is the slant height
    return (3.14*x*y)

def arcrcl(x):
    # Area of Circle
    # x is the radius
    return (3.14*x*x)

# PERIMETER OF SHAPES
def perrect(x,y):
    # Perimeter of rectangle
    # x is the length
    # y is the width/breadth
    return (2*(x+y))

def pertrngl(x,y,z):
    # Perimeter of Triangle
    # x,y,z are the three sides of traingle
    return (x+y+z)

def persqr(x):
    # Perimeter of Square
    # x is the sides of square
    return (4*x)

#end of the module