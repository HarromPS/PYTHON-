# to define class method use @classmethod decorator
# Note: 1st args in any instance method is the instance

class Emp:
    # class variable
    company = "Apple";

    def __init__(instance,name):    # (self/obj/aloo)
        instance.name=name;

    def chagCom(cls, newCmp):       # cls = self
        cls.company = newCmp;       # refers to the local instance variable

    # to define class variables
    @classmethod
    def changeCompany(cls, newCompany): # cls = class instance => Emp
        cls.company = newCompany;

obj = Emp("A");
print(obj.company);     # refers to class level variable as no local variable is not present this time
obj.company = "Tesla";
print(obj.company);     # refers to local variable as a company variable is created now

# But class variable is not changed
print(Emp.company);

# to change class variable
obj.changeCompany("Tesla");
print(Emp.company);