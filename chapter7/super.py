# super() function keyword: refers to the parent class

class Parent:
    def __init__(self,name,id):     # only name & id is required in this class
        self.name = name;
        self.id=id;

class Child(Parent):
    def __init__(self,name,id,age): # only name & id & age is required in this class
        super().__init__(name,id);
        self.age=age;

    def callMethod(self):
        print("Super() child is called");

class GrandChild(Child):
    def __init__(self,name,id,age,salary):  # name, id, age, salary is required in this class

        # pass the super() class parameters to it using super() keyword
        super().__init__(name,id,age);
        super().callMethod();
        self.salary=salary;

obj1 = Parent("Amit",21);

obj2 = Child("Amit",21,10);

obj3 = GrandChild("Amit",21,10,1000);
