# Constructor: a special method used to create object & initialize variables of an object
# Automatically gets called when an object is created & if not made, interperter automatically creates it.

class A:
    def __init__(self):     # default constructor
        self.name="hello";
        self.occ = "developer";


    # def __init__(self,name,occ):     # parameterized constructor (3 params)
    #     self.name=name;
    #     self.occ = occ;

    def info(self):
        print(f"{self.name}");

# creating an object using default constructor
obj1 = A();                 # only one constructor allowed
obj1.info();

class B:
    def __init__(self,name,occ):     # parameterized constructor (3 params)
        self.name=name;
        self.occ = occ;

    def info(self):
        print(f"{self.name}");

# creating an object using default constructor
# obj2 = B();                             # Error
obj2 = B("Amit","Developer");           # (1 object, 2 args) = (3 params)
# obj2 = B("self","Amit","Developer");           # Error
obj2.info();