import random
import string

# return a string
a=string.ascii_letters;
print(type(a[0]));

n=5;
for i in range(n):
    l= [];
    for j in range(n):
        l.append(random.choice(a));
    for ele in l:
        print(ele,end=" ");
    print();

lst=[];
for i in range(10):
    lst.append(random.randrange(0,10));

lst.sort();
lst.reverse();
print(lst);
