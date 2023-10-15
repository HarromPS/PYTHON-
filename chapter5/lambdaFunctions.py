# Lambda functions: these are the functions with no names
# Syntax : lambda (args) : expression

def sq(x):
    return x*x;

res = sq(2);
print(res);

# lambda function
square = lambda x: x*x;

res=square(3);
print(res);

# we can pass function as an argument to another function
def fun(funInner,val):
    return 1+funInner(val);

def funInner(val):
    return val+1;

res=fun(funInner,val=12);
print(res)