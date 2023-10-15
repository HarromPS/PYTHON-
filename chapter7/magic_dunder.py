# Magic/Dunder methods:
# Created using __(underscore-underscore) at start & end

# used specially in classes, to customize class behavoiur
# used to implements methods like addition, subtraction (used in operator overloading), descriptors, properties
# good for encapsulation

class emp:
    name = "Hello";

    # 1) __init__() : automatically called when an object is created
    # used as emp()
    def __init__(self,name):
        self.name = name;

    # 2) __len__() : used to return the length of an object
    # len(obj)
    def __len__(self):
        i=0;
        for c in self.name:
            i=i+1;
        return i;

    # 3) __str__() & __repr__():
    # str()- used to convert an object to a string repersentation
    # e.g - This is an object of <Emp class>
    # repr()- to get a string repersentation of an object of its recreation procedure
    # e.g - Emp("Name");

    # Note: i fstr is not defined, then reper is called
    def __str__(self):
        return f"This is an object of <emp class>";

    def __repr__(self):
        return f"emp('Hello')";

    # 4) __call__() method: makes an object callable, if not present error
    # allows to create callable object which behaves as functions
    def __call__(self,args):
        print("Object made callable like a function, ",args);


e=emp("Hello");
print(len(e));

print(str(e));
print(repr(e));

e([1,2,3]);