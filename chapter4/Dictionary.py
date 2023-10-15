# Dictionary
# ordered collection(printed in same order) of data items stored in key-value form
# in older version of python it was unordered collection of data items
# seperated by comma, enclosed in curley braces like JS object

dic = {
    "A": "one",
    "B": True,
    32: "7"
};

# Accessing items

# particular value Using square braces
print(dic["A"]);

# gives error if key is not found
# print(dic["Z"]);

# particular value Using .get() method
print(dic.get("A"));
# do not give error

print(dic); # all key value pairs
print(dic.keys()); # keys only

# OR

for keys in dic:
    print(keys);

print(dic.values()); # values only

# OR

for vals in dic.keys():
    print(dic[vals]);

# OR
for vals in dic.values():
    print(vals);

# accessing all key values pairs
print((dic.items()));
print(type(dic.items()));

# OR
for (key,value) in dic.items():
    print(key,value);