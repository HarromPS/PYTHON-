# loops : used to iterate a common step

# 1) for loops : can iterate overa sequence, can iterate iterable objects
# strings, list, sets, tuple, dictionary

name = "Hello";
for i in name:
    print(i,sep="",end=" ");

print();
name = ["A",2,3,4,["Hello",None]];
for k in name:
    print(k,sep="",end=" ");

print();
# using range function
for i in range(5):      # start 0 to n-1
    print(i,sep="",end=" ");

print();
for i in range(2,15):      # start a to n-1
    print(i,sep="",end=" ");

print("Herer");
for i in range(1,15,4):      # start a to n-1 & skip 4 steps including current step
    print(i,sep="",end=" ");
# 'included'
# '2' 3 4 '5' 6 7 '8' 9 10 '11' 12 13 '14'

print();
for k in range(10):
    print((k+1)*2,sep="",end=" ");

print();
# While loops
i=1;
# increment loops
while(i<10):
    print(i,sep="",end=" "); i=i+1;

print();
# decrement loops
i=10;
while(i>0):
    print(i,sep='',end=' '); i=i-1;

print();
# else in while loops
# when iterpreter gets out of loop then else statement is executed
while(i<10):
    print(i,sep='',end=' '); i=i+1;
else:
    print("Existed");

# do-while loops are not available in python
# but we can emulate do-while loops
i=1;
print(i,sep='',end=' '); i=i+1;
while(i<10):
    print(i,sep='',end=' ');
    i=i+1;

print();
# break: exit out of loop
i=1;
while(i<10):
    if(i==5):
        print("Exit out of loop");
        break;
    print(i,sep='',end=' ');
    i=i+1;

# continue: exit out of that iteration
i=1;
while(i<10):
    if(i>=10):
        print("Exit out of loop");
        continue;
    print(i,sep='',end=' ');
    i=i+1;

# do-while loop emulation
print();
i=10;
while True:
    print(i,sep='',end=' ');
    i=i+1;
    if(i>20):
        break;