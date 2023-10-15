# We use constructors to assign variables at the time of object creation
# if some other formats are given, we have to then parse 1st then pass to constructor
# to make it simple we use class methods as alternatives of constructors

class Emp:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;

    @classmethod
    def fromString(cls,str):
        # 1st parse, then pass to constructor
        nm = str.split(",")[0];
        age =int(str.split(",")[1]);       # also typecasted

        # return a new Instance
        return cls(nm,age);

obj1 = Emp("amit",12);
print(obj1.name,obj1.age);

string = "Ajit,21";
obj2 = Emp.fromString(string);  # new instance retruned
print(obj2.name,obj2.age);
