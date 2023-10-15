# Tuple
# Ordered collection of different datatype elements, multiple value in a single variable
# Seperated by comma, enclosed in round braces
# Are Immutable

tpl = (1,2,3);
print(type(tpl),tpl);

tpl2 = (1);         # single element is a integer
print(type(tpl2),tpl2);

tpl3 = (1,);         # to create a tuple, a comma is necessary
print(type(tpl2),tpl2);

# Accessing tuple elements
tple = (1,2,3,"Hello",True);
print(tple[0],tple[1],tple[2]);

# Properties
print(len(tple));

# Negative indexing
print(tple[-2]);

# Membership Operation
if(3 in tple):
    print("Yes");
else:
    print("No");

# Operations on tuple Gives a new Tuple
# tuple slicing
tp=tple[1:4];
print(tp,type(tp));