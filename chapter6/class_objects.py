# 1) Procedural oriented programming: uses functions & runs in a procedural oriented manner
# 2) Object oriented programming: uses classes and functions

# Creating class
class Employee:

    # default values and can be changed later
    name="Amit";
    occupation="Software Developer";
    def info(self):
        print(f"{self.name} is a {self.occupation}");

# self  = this keyword
# refers to the calling object & used to access variables belongs to the class
# must be provided as an extra parameter inside class function defination

# Creating an object
obj = Employee();       # constructor function

# Accessing & updating values
print(obj.name);        # access using .(dot) operator
print(obj.occupation);
obj.info();

obj.name = "Rahul";
obj.occupation = "Problem Solver";
print(obj.name);
print(obj.occupation);
obj.info();