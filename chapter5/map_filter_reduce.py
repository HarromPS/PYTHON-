# Map(), Filter(), Reduce():
# are higher-order functions used in advance list manipulation

# 1) map(): function runs for each argument & returns a map object & is converted into list
# Syntax: map(function, iterable)

def fun(x):     # x is element of the list passed as 2nd args
    return x+1;

lst = [1,2,3,4];
newList = map(fun,lst);     # returns map object
newList = list(newList);    # converted into list
print(newList);

# ////////////////////
# lambda function
newList = list(map(lambda x: x*2, lst));
print(newList);

# filter :
# Syntax: filter(predicate, iterable);      predicate- a function returns true/false
def fun(x):
    return not x%2;

newList = filter(fun,lst);     # returns filter object
newList = list(newList);    # converted into list
print(newList);

# ////////////////////
# lambda function
newList = list(filter(lambda x: x>1, list(map(lambda x:x+18, lst))));
print(newList);

# reduce : reduces the whole list to a single value
# Syntax:
from functools import reduce

def fun(x,y):
    return x+y;

newval = reduce(fun, lst);
print(newval);

# ////////////////////
# lambda function
newval = reduce(lambda x,y: x+y, lst);
print(newval);