'''
List is a ordered collection of different datatypes
Seperated by comma, enclosed by sq. braces
Changable (Mutable)
'''

lst=["lst","B","C","D"];
print(lst);
lst=[1,2,3,4];
print(lst);
lst=["A",1,"C",2];
print(lst);

# Accessing values seperately
print(lst[0],lst[2]);

# length of list
print(len(lst),type(lst));

# Negative indexing
print(lst[-3]);
print(lst[len(lst)-3]);
print(lst[4-3]);
print(lst[1]);

# List slicing just like string slicing
print(lst);
print(lst[:]);
print(lst[0:]);
print(lst[:len(lst)]);

lst=[1,2,3,4,5,6,7,8,9,10,11];
# Range items
# Syntax: lst[start: end: jumpIndex(skips index)];
# 1, 1+3(4), 4+3(7), 7+3(10), 10+3(13)
# 2, 5, 8 < 9

print(lst);
print(lst[1:9:3]);
print(lst[1:9:2]);
print(lst[3:10:4]);

# List comperhension
# creating a new list from iterable e.g other list, tuple, dict, set, dict, etc.
# list2 = [Expression(item) for i in iterable if condition];

list2=[i for i in range(5)];
print(list2);

list2 = [(i*i) for i in range(6) if(i%2==0)];
print(list2);
