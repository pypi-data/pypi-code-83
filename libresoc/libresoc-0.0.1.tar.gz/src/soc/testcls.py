class Base:
    def __init__(self):
        print("base name", self.__class__.__name__)

class Derive(Base):
    pass

x = Base()
y = Derive()

name = "CompALUOpSubset"
print (name[4:-8].lower())

