# getter: used to access the values of the objects property
# helps to use functions return value as an object property

class Class:
    def __init__(self,val):
        self.value=val;

    # @property decorator
    @property
    def value_10(self):         # method as a property
        return self.value;

# Note: getter don't have parameters & cannot set any value
# best for Encapsulation & Data Validation

obj = Class(10);
print(obj.value);
print(obj.value_10);

class Class2:
    def __init__(self,val):
        self.value=val;

    @property
    def value_10(self):
        return self.value;

    # @method_name.setter
    @value_10.setter
    def value_10(self,newval):
        self.value=newval;

# Note: setter gets parameters & do not returns
obj2 = Class2(11);
print(obj2.value);
print(obj2.value_10);

obj2.value_10=12;           # assign as a property
print(obj2.value_10);

