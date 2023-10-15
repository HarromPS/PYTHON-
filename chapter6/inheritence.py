# Inheritence: Derives the parent class

# child class can have access & can inherits to public and protected methods and properties
# also child class can have its own methods

class Parent:
    def __init__(self,val):
        self.val=val;

    def method(self):
        print(f"Value is: {self.val}");


class Child(Parent):
    def __init__(self, val1):
        super().__init__(val1);      # requirement of Parent class

    def show(self):
        print(f"Child method");


class grandChild(Child):
    def __init__(self, val1):
        super().__init__(val1);             # requirement of Parent class

    def show(self):             # same named method is Overrided in child class
        print(f"Grand Child method");

    def show2(self):
        print(f"grandChild method");

objP = Parent(10);
objP.method();

objC = Child(12);     # provide parameters for 1st Parent parameterized constructor
objC.method();
objC.show();

objGC = grandChild(1);      # provide parameters for 1st Parent parameterized constructor
objGC.show();
objGC.show2();
objGC.method();