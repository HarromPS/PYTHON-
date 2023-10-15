# local variable:
# varibles created inside a function when it is called & destroyed as a function terminates
# is only accessible inside that function

# global variable:
# varibles created outsied a function & destroyed when program ends
# is accessible inside every function

x=1;    # global
print(x);

def fun():
    x=10;   # local
    print(x);

fun();
print(x);

# global keyword: mentions that a variable is a global scoped var inside a function
y=10;
print(y);

def fun2():
    global y;
    y=100;  # changed

fun2();
print(y);   # avoid modifying global variables, is a good practice