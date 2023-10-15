# Variable -> containers to store values
a = 1;      # 1 is stored in memory location with a name 'a'
print(a);

# Datatype -> specifies what type of data a variable holds

# 1) Numeric: int, float, complex
a = 12;
print(a, type(a));        # integer

a = 1.2023;
print(a, type(a));        # float

a = complex(10,2);
print(a, type(a));        # complex

# Text: str
a = 'A';
print(a, type(a));
a = "Hello";
print(a, type(a));       # string

# boolean: True, False
a = True;
print(a, type(a));
a = False;
print(a, type(a));         # boolean

a = None;
print(a, type(a));      # None type

# Note: only same data types are concatenated in Python
a = 12;
b = "Hello";
# print(a+b);     # type error

# Sequenced datatype: list, tuple, dictionary

#list : ordered collection of different datatype seperated by comma
# & enclosed in sq braces& are mutable (array in JS)

list1 = ["Hello", [120,True,None], 1.21, 'A'];
print(list1);

# tuple: same as List but immutable, enclosed in simple braces, & of same datatype
tuple1 = ("parrot", ("joker"), "ABC", "abc");
tuple1 = ("parrot",10, ("joker"), "ABC", "abc");
print(tuple1);

# dict : dictionary -> unordered collection of key value pairs like Objects in JS