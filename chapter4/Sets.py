# Sets:
# unordered collection of data different items
# stores unique(non-repetative) objects
# enclosed in curley braces & seperated by commas
# unchangeble like a marbel stored in a bag of marbles
# cannot be accessed using index

s = {2,3,3,3,3,4,5,6};
print(s); # {2,3,4,5,6}

info = {1,"a",True,None,"lol",False,123};
print(len(info)); #ordered is not maintained & True is not stored in sets

# Quick quiz: print empty set
s = {};
print(s,type(s));   # prints empty dict

# to print empty set
s = set();
print(type(s));

# Accessing elements in a set
for item in info:
    print(item,sep='',end=' ');