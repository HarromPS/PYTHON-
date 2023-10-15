# user inputs are taken using "input()" function
# the input is taken as a input string value

# Syntaxl:
print("Enter a name:",sep=" ",end=" ");
a = input();
print(a);

# Note: input() function returns a string, hence the input needed to be coverted into
# another datatype
a = int(input("Enter a number: "));
print(a);

# Exercise 1 (re-attempt)
num1 = float(input("Enter first number: "));
num2 = float(input("Enter second number: "));

print("The value of",num1,"+",num2,"is",num1+num2);
print("The value of",num1,"-",num2,"is",num1-num2);
print("The value of",num1,"*",num2,"is",num1*num2);
print("The value of",num1,"/",num2,"is",num1/num2);
print("The value of",num1,"%",num2,"is",num1%num2);
print("The value of",num1,"**",num2,"is",num1**num2);
print("The value of",num1,"//",num2,"is",num1//num2);