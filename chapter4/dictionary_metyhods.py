dic = {
    'A': 'one',
    'B': 'two',
    32: "om"
};
d1 = {
    10: 12,
    11: 13
};

d2 = {
    "a": "A",
    "b": "B"
};

# 1) .update( {key: value} )
dic.update({"age":10});
# OR
d1.update(d2);
print(dic,d1,d2,sep="\n");

# 2) .clear() - removes all the key-value pairs from the dictionary
dic.clear();
print(dic);
dic = {
    'A': 'one',
    'B': 'two',
    32: "om"
};

# 3) .pop(key) - removes a particular key-value pair given as a parameter & returns value
x=dic.pop("A");
print(x);
print(dic);
dic.update({"A":"one"});

# 4) .pop_item() - removes the last item in dictionary
dic.popitem();
print(dic);

# 5) del keyword - deletes the whole dictionary
# Note: if del is used by passing a parameter as a key, then it works as .pop(key) method
del dic["B"];
print(dic);

del dic;    # deletes the whole dictionary
# print(dic);   # gives NameError