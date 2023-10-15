# Operator Overloading: allow to redefine the behaviour of mathematical & comparison operators
# using Dunder/Magic Methods

class vector:
    def __init__(self,i,j,k):
        self.i=i;
        self.j=j;
        self.k=k;

    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k");

    # multiplication dunder method
    # def __add__(self,obj):
    #     # returns a string
    #     return f"{self.i + obj.i}i, {self.j + obj.j}j, {self.k + obj.k}k";

    def __add__(self,obj):
        # returns a vector
        return vector(self.i + obj.i, self.j + obj.j, self.k + obj.k);

    def __sub__(self,obj):
        return vector(self.i - obj.i, self.j - obj.j, self.k - obj.k);

    def __mul__(self,obj):
        return vector(self.i * obj.i, self.j * obj.j, self.k * obj.k);

    def __truediv__(self,obj):
        return vector(self.i / obj.i, self.j / obj.j, self.k / obj.k);

obj1 = vector(1,2,3);
obj1.show();

obj2 = vector(11,12,13);
obj2.show();

# add
x=(obj1+obj2);
x.show();

# sub
x=(obj1-obj2);
x.show();

# mul
x=(obj1*obj2);
x.show();

# div
x=(obj1/obj2);
x.show();

