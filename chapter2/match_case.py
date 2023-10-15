# Match case(Switch case in C/C++)are used for different cases
# Syntax:

x=int(input("Enter a number: "));

match x:
    case 0:
        print("x is",x);
    case 1:
        print("x is",x);
    case 2:
        print("x is",x);
    case 3:
        print("x is",x);

    # default case (if none of the case executes then default case is executed)
    case _ if(x>20):
        print("x is greater");
    case _ if(x!=12):
        print("x is less");
    case _:
        print("Default case");

