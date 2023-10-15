# Self parameter:
class Self:
    def __init__(self,nm):
        self.name = nm;
    def show(self):
        print(self.name);

obj = Self("Self");
Self.show(obj);     # now the parameter is matched with the arguments

# Instanance variable: defined for a instance of a class i.e on a local level

class Local:
    def __init__(self,nm):
        self.name = nm;
    def show(self):
        print(self.name);

obj = Local("Name");
obj.newLocalvar = "new";
obj.show();
print(obj.newLocalvar);

# Class Instance: variable on the class leval & is shared among all the instances of the class
class Classlevel:
    company = "Google";

    def __init__(self,nm):
        self.name = nm;

    def show(self):
        print(f"{self.name}, {self.company}");

# Note: 1st sees for local instance, if not found, it goes for class instance
obj1 = Classlevel("obj1");
obj1.company = "Apple";      # creates a local instance
Classlevel.show(obj1);

obj2 = Classlevel("obj2");
Classlevel.show(obj2);      # uses class level variable
