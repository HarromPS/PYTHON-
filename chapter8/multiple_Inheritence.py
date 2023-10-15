# Multiple Inheritence: more than one parent
# follows a MRO (method resolution operator) to avoid ambuiguity
# order of inheritence matters-> mro(): 1st sees child, father then mother

class Father:
    def sports(self,sport):
        # in percentage 00-100  increasing fareness
        self.color = sport;

class Mother:
    def cooking(self,food):
        self.color = food;

class Child1(Father,Mother):
    def __init__(self,name,age):
        self.name = name;
        self.age=age;

    def color(self,color):
        self.color = color;

class Child2(Mother,Father):
    def __init__(self,name,age):
        self.name = name;
        self.age=age;

    def rating(self):
        print(1);

c1 = Child1("n1",1);
print(Child1.mro());

c2 = Child2("n2",2);
print(Child2.mro());