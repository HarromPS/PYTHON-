# f-Strings
# used in String formatting
# Just like String template in JS

# In old Python,
str = "My name is {} and I am {}";
name = "A";
prof = "B";
result = str.format(name,prof);
print(result);

# f-string introduced in PEP 498, allows more precise control over formatting
# such as specifing the no of decimal place,etc
# Provides a convinent way to enbed Python expression directlty inside strign literal for formatting
# Prefix "f" before a string -> becomes f-string

# e.g
name = "Amit";
age = 12;
str = f"My name is {name} and I am {age} years old";
print(str);