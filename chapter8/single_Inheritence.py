# Single Inheritence: Inherits only parent class
# inherits all attributes & behaviours

class Animal:
    def __init__(self,name,type):
        self.name=name;
        self.type=type;

    def sound(self):
        print("sound made by the animal");

class Dog(Animal):
    def __init__(self,name,type):
        self.name=name;
        self.type=type;

    def sound(self):
        print("Bark!");

class Cat(Animal):
    def __init__(self,name,type):
        self.name=name;
        self.type=type;

    def sound(self):
        print("Meow!");

A = Animal("Animal","Animal");
A.sound();

d=Dog("Dog","Domestic");
d.sound();

c=Cat("Cat","Domestic");
c.sound();