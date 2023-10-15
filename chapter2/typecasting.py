# TypeCasting - conversion of one datatype into another datatype
# methods used - int() float() str() ord() hex() oct() tuple() set() list() dict()

a = "1";
b = "2";
print(a+b);     # concatenation of two strings

# conversion from string to valid numbers
a=int(a);
b=int(b);
print(a+b);

a=1;
b=2;
print(a+b);     # operation on two numbers

# Two types of typecasting
# Explicit (by user/programmer)
# Implicit (by the python interpreter itself)
# Python Interperter converts the lower order types into higher order types

c = 2;  # integer
d = 1.2;  # float
print(c+d, type(c+d));      # integer + float = > float