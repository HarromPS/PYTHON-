# Strings: like array of characters enclosed in "" or ''
# used when working with Unicode characters

name = "Hello";
friend = 'Amit';
print(name,friend);

# Quote inside quote
name = "He said, 'I am a boy'";
print(name);
# OR
name = "He said, \'I am a boy\'";
print(name);

# Multiline Strings
name = '''This is a Multiline String
This is again a multiline string''';
print(name);

# name = " Hell a ;     EOL(end of line) error(ending not found)

# looping the string
for characters in name:
    print(characters,sep="",end="");

# Accessing character of a string
name = "Hello";
print();
print(name[0]);
print(name[1]);
print(name[2]);
print(name[3]);
print(name[4]);

a=["jwjiwj"];
print(len(a[0]));