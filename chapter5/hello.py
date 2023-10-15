# if __name__ == " __main__ ":
#       functions...

# it is a idiom used in Python Scripts(code) to check if code being is run directly
# OR run by importing to another script as a module

'''
hello.py

def fun():
    print("hello");

fun();

/////////////////
main.py

import hello

hello.fun();

// now we think fun() will run only one time but runs twice
  As All the Imported code runs automatically by just importing i.e
  some functions runs automatically by just importing -> Hacking malware like

To avoid this:
we use if __name__ = "__main__"

if run directly in same script: __name__ is set to string "__main__"
else : __name__ is set to name of module imported hello

'''

'''

Thus,

hello.py

def fun():
    print("hello");

print(__name__);
if __name__ == "__main__":
    fun();

/////////////////
main.py

import hello

hello.fun();

// will only one time


'''

# def fun():
#     print("hello");

# fun();        RUN ONCE

def fun():
    print("hello");

print(__name__);    # run directly : __name__ => __main__
if (__name__ == "__main__"):
    fun();

    # is vs ==
    # both are comparsion operators
    # is: compares exact memory locations
    # == : compares the value

    a=4;
    b="4";
    print(a is b);
    print(a == b);

    a=4;
    b=4;
    print(a is b);
    print(a == b);

    a=None;
    b=None;
    print(a is b);
    print(a == b);