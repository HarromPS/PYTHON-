# for loops with else
# an else statement executed after the whole loop is executed.
for i in range(5):
    print(i);
else:
    print("Loop exited");

# Note: when loop successfully completes only then else statement is executed
for i in range(5):
    print(i);
    if (i==3):
        break;
else:
    print("Loop Exited");

# Can run same with while loops
i=0;
while(i<5):
    print(i);
    i=i+1;
else:
    print("loop existed");

# do while
i=0;
while(True):
    print(i);
    if(i>5):
        break;
    i=i+1;
else:
    print("loop existed");