# Types of files : Text/Binary(images, binary, PDFs, etc);

# open a file  , two arguments
f = open("file.txt",'r');

# Modes
# read "r": default mode, gives error if file does not exists
text = f.read();
print(text);

# write "w": creates a new file if not exists, else writes a file after clearing all the contents
f=open("file.txt","w");
# f.write("This is new content");

# append "a": adds content at end of the file,  creates a new file if not exists
f=open("file.txt","a");
f.write("\nAppend");

# create "x": creates a file, gives error if file exists
# f=open("file1.txt","x");

# Closing a file
f.close();

# "with" statement: alternate of opening & closing a file
with open("file1.txt",'a') as f:
    f.write("New content for new file\n");
    f.close();