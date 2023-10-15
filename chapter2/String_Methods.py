# Strings are Immutable(can't be changed)

# 1) length
name = "Hello World";
print(len(name));

# 2) upper() converts to uppercase, original name string is unchanged
print(name.upper());

# 3) lower() converts to lowercase
print(name.lower());

# 4) rstrip() removes any trailing character & not from front
name = "!!! Hello !!! "  # !!! Hello
print(name.rstrip("!"));

# 5) replace(to be replaced, to place) replaces all the occurances of given parameter string
name = "he is a man, she is a girl";
print(name.replace("is", "are"));

# 6) split(split a/c) seperates the string & returns a list of seperated sub-strings
name = "A, B, C, D";    # ["A","B","C","D"]
print(name.split(","));

# 7) capitalize() converts 1st letter to uppercase & rest to lowercase
name = "he is a man, she is a girl";
print(name.capitalize());

# 8) center(value, put in place) aligns the string from left & right(padding) as per the parameter
name = "Welcome Home";
print(name.center(20));     # len = 12, |20-12|=8 => 8/2 4(left & right)
print(name.center(20,"."));     # len = 12 (12-12)
print(len(name));

# 9) count(element) count the occurance of a sub-string
name = "he is a man, she is a girl";
print(name.count("is"));

# 10) endswith(value) true if a string ends with a given string parameter
print(name.endswith("girl"));
name="Hello";
print(name.endswith("l",2,3));

# 11) find(value) return "index" if a sunstring is found, else -1
name = "he is a man, she is a girl";
print(name.find("is"));

# 12) index(value,start,end) same as find() but return error if not found
print(name.index("she"));
print(name.index("s",3,8));

# 13) isalnum() return true if all characters in a string are alpha-num A-Z,a-z,0-9
name="123abc";
print(name.isalnum());

# 14) isalpha() return true if all characters are alphabets A-Z,a-z
name="abc";
print(name.isalpha());

# 15) islower() returns true if all characters are lower case
print(name.islower());

# 16) isupper() returns true if all characters are upper case
name=name.upper();
print(name.isupper());

# 17) isprintable() returns true if the strign is printable
name = "Hello\n";
print(name.isprintable());

# 18) istitle() returns true if 1st letter of each word in a string is uppercase
name = "i Am A Boy";
print(name.istitle());

# 19) isupper() & islower() return true if all characters are upper/lower
name="ABC";
print(name.isupper());
print(name.islower());

# 20) startwith(value) returns true if string starts with a given string parameter
name = "i Am A Boy";
print(name.startswith("Am"));

# 21) swapcase() converts all uppercase with loercase & vice versa
print(name.swapcase());

# 22) title() converts all 1st letter of each word to uppercases & rest lowercase
name = "i am a boy & she is a girl";
print(name.title());

# 23) Membership operation
if "a" in name:
    print("Yes");
else:
    print("No");