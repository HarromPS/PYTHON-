# scripts
print("Hello World");
print(5);
print(10+10);
print(0/12);
# print(12/0);

# Interperter interprets code line by line, if error, stops until the error is fixed
# print(jpwew);

''' # This is a comment '''

# Escape sequences
print("\nThis is a newline escape character\n");  # Printing a newline character
print("This is a newline \'escape\' character");  # Printing a single quote character
print("This is a newline \"escape\" character");  # Printing a double quote character
print("This is \a audible bell \"escape\" character");  # Printing a audible bell character
print("This is \f form feed \"escape\" character");  # Printing a form feed character
print("This is \b backspace \"escape\" character");  # Printing a backspace character
print("This is \v vertical tab \"escape\" character");  # Printing a vertical tab character
print("This is \t horizontal tab \"escape\" character");  # Printing a horizontal tab character

# print() function
# print(object(s), seperator, end-end, file-file, flush-flush);
print("\none","two","etc"); # multiple values can be passed as an argument to this function
print("\none","two","etc",sep="@"); # 2nd parameter seperator to seperate multiple values(" " default)
print("\none","two","etc",sep="@",end="\rThis is end"); # 3rd parameter what to print at the end of statement(\n default)
# file = to read into file (sys.stdout default)