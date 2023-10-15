# Custom Error
# Using raise keyword like throw keyword

# a = int(input("Enter: "))
# if(a < 5 or a > 9):
#     raise ValueError("Enter between 5 and 9")
# print("Ends")

# a = int(input("Enter: "))
# if(a > 9 and a < 15):
#     raise ValueError("Enter between 9 and 15")
# print("Ends");

# Defining Custom errors
# by deriving class from built-in Exception class


# class customExceptionClass(Exception):
#     # code
#     pass

#     try:
#         # code
#     except:
#         # code

# Quick Quiz:
# create a program if a user inputs 'quit', then no error else error for any other input other than integer

# try:
a=input("Enter: ");

if(a=="quit"):
    print("No error");
elif(a.isalpha()==False):
    print("No error");
else:
    raise ValueError("Enter interger except 'quit' ");
