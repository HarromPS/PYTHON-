# Decorator functions: returns a modified version of an existing function & not changed original function.

# Syntax: takes another function, returns a function with modifications => Decorated function

def greet(fun):
    def modified():
        print("Modifing");

        # calling args function
        fun();
        print("Thank you");

    # returning modified function
    return modified;

# 1-way to use decorated function
@greet          # @ sign- imp
def hello():
    print("hello");

# calling modified function
hello();

# 2-way to use decorated function: by commenting @greet line
hello = greet(hello);
hello();

# OR greet(hello)()
# calling hello, then returned modified function


# Modifing add function

def greet1(fun):
    def modified1(*args,**kwargs):
        print("Adding");

        # calling args function
        fun(*args);
        print("Done");

    # returning modified function
    return modified1;

#way 1
@greet1
def add(a,b):
    print(a+b);

add(1,2);

# way 2
add = greet1(add)(1,2); # greet call, then modified call args (1,2) for add
# add = modified

# add(1,2);     # error


# Used in logging, memorization, access control
import logging;     # logs function call before & after original function is called

def log_fun(fun):
    def decorated(*args,**kwargs):
        logging.info(f"Calling {fun.__name__} with args={args}, kwargs={kwargs}");
        result=fun(*args,**kwargs);
        logging.info(f"{fun.__name__} returned {result}");
        return result;
    return decorated;

@log_fun
def myFun(a,b):
    return a+b;

print(myFun(1,2));