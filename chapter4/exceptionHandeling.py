# Exceptions are the unexpected/unwanted events occurs while executing a program
# example data from server do not reaches due to network issues
# we use Try Except to handle the errors

try:
    a=int(input("Enter a Number:"));
except:
    print("No is not a Integer");


try:
    a=int(input("Enter a Number:"));
except Exception as e:
    print("No is not a Integer",e);

# multiple & specific exceptions
num=[1,2,3,4];
try:
    for i in range(5):
        print(num[i]);
except ValueError as e:
    print(e);
except IndexError as e:
    print(e);

