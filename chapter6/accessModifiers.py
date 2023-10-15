# By default, all variables are Public in Python
# There is no such concept of Access protection in Python, just conventions

# Public: accessed everywhere
class Public:
    def __init__(self,nm):
        self.name = nm;

obj1=Public("Public name");
print(obj1.name);

# Private: Access within class, outside also, but generally not to be accessed/modified outside
class Private:
    def __init__(self,nm):
        # to create a private variable
        self.__name = nm;           # known as Weak Internal Use Indicator (double underscore)

obj2=Private("Private name");
print(dir(obj2));       # shows all vars & methods
# print(obj2.__name);   # not accessed outside

# To access -> obj._ClassName__VariableName (Name Mangling)
print(obj2._Private__name);

# Name Mangling: Indirect accessed i.e with double underscores
# To protect variables from getting overriden , therefore Name of class-private
# Superclass-private vars is Transformed by addition of Single Underscore & Double Leading Underscore

# Protected: accessed within or subclass
class Protected:
    def __init__(this,name):
        this._name = name;      # single underscore

class childPro(Protected):
    pass

obj3 = Protected("Protected name");
obj4 = childPro("Protected name");

print(obj3._name);      # no name mangling
obj4._name = "child Pro name";
print(obj4._name);      # no name mangling