# In c++/ java static methods are methods belongs to the class & not instance of class
# In Python, static methods are made using @staticmethod decorator
# No need of 'self' argument
# used as utility function & for shipping

class Math:
    def __init__(self,name):
        self.name = name;

    @staticmethod       # decorator
    def add(a,b):       # No need of 'self' argument
        return a+b;

obj=Math("A");
print(obj.name);
print(obj.add(1,2));
print(Math.add(11,12));
# print(add(11,12)); # give error as no global method