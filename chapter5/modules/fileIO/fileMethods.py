# methods in file io
# 1) readline(): reads file line by line
f=open("file.txt","r");
newlst=[];
while(True):
    line=f.readline();
    newlst.append(line);    # reading file from front & adding to end
    print(line,type(line)); # returns string
    if(not line):
        # Note: empty string is false
        print(line);    # empty == false
        break;
print(newlst);

# Note: + not used to concatenate string & integer, but can multiply
s="A";
s*=3;
# print(s);

# writeline(): used to write sequence of iterable strings, but do not adds newline between strings
f=open("file.txt","a");
lst=["\nMy\n","Name\n","Is\n","Harry\n"];
for strs in lst:
    f.writelines(strs);

f.close();

with open("file2.txt","r") as f:
    while(True):
        lines=f.readline();
        if(not lines):
            break;
        # print(lines.split(","));
        m1=lines.split(",")[0];
        m2=lines.split(",")[1];
        m3=lines.split(",")[2];
        print(f"Marks {m1}, {m2}, {m3}");
    # reading the file contents


# seek() & tell(): functions used to work with file pbjects & their positions within a file
# such as file, pipes & in-memory buffers

with open ("file1.txt",'r') as f:

    # seek() method: used to move the control b bytes in a file forward or backward
    f.seek(10); # moves 10 bytes forward
    print(f.read(5)) # reads 5 bytes from the file after 10th position

    # tell(): tells the current position of control in a file in bytes
    print(f.tell());    # 15

with open ("file.txt",'a') as f:
    # truncate() shortens the file in bytes, but open in "w" or "a"
    f.writelines("hello\n,world");
    f.truncate(50);
