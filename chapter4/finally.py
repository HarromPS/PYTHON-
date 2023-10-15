# Finally: Used for cleanups, always executed irrespective of error occured or not
try:
    a = int(input("Enter a no: "));
except:
    print("Error");
finally:
    print("Always executed");

# Best example
# used for doing conclusions,closing database connections, ending program execution with a message
def fun():
    try:
        a=int(input("Enter "));
        return 1;
    except:
        print("Errors");
        return 0;
    finally:
        print("Always executed");

    # without finally this statement never executes
    print("Always executed");


x = fun();
print(x);
