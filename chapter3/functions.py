# There are two types functions in python
# 1) Built-in functions: defined & pre-defined codes
# .eg print(), range(), tuple(), set(), dict(), sum(), etc;

# Note: Function overloading does not work in C/Python

# 2) User defined functions
# Syntax:
def greater(a,b):
    if(a>b):
        print(a,"is greater than",b);
    else:
        print(b,"is grater than",a);


def sumOf(a,b,c):
    return a+b+c;

greater(10,20);
s=sumOf(12,12,12);
print(s);
# print(sumOf(1,2));
# print(sumOf(1,2,3));
# print(sumOf(1,2,3,4));

# Arguments in functions

# 1) Default arguments: Provide default values to the arguments while creating a function
# & is used if no parameter is passed
def fun1(a=10, b=12):
    print(a,b);

fun1();

# if args passed, then default values are overrided/ignored
fun1(2,2);
# particular arguments
fun1(a=668);
fun1(b=9);

# 2) Keyword arguments: args as key-value pairs
# Interpreter identifies args as name, hence order of passing args does not matters
def fun2(a,b,c):
    print(a,b,c);

fun2(a=32,b=32,c="Hello");
fun2(a=32,b="po",c=True);

# 3) Required arguments: if no key-value pairs, then mandatory to pass arguments in
# correct order & proper no. of args
def fun3(a,b,c):
    print(a,b,c);

fun3("Hello",1,True);

# 4) Variable-Sized arguments:
# a) Arbitary arguments: Tuple argument
# put * before parameter name, function accesses args by processing as tuple
def fun4(*args):
    for i in args:
        print(i);
    if(len(args)<=2):
        print(args[0],args[1]);
    else:
        print(args,type(args));

# b) Keyword Arbitary arguments: Dictionary argument
# put ** before parameter name, function accesses args by processing as dict
def fun5(**args):
    print(args["x1"],args["x2"],args["x3"]);

fun5(x1="one",x2="two",x3="three");

# 5) return statements: used to return a value to calling function
def retFun():
    return 1;   # 1st is allowed & rest is ignored
    return 2;
    return 3;

print(retFun());


# if a function body is not defined then we can pass the body
def hello():
    pass;