# All methods changes the oroginal list

lst=[1,2,2,2,3];
print(lst);
# 1) append(element): adds a new element to the end of the existing list
lst.append(4);
print(lst);

# 2) sort(): sorts list in increasing order
lst.sort();
print(lst);

# 3) reverse(): reverses the list
lst.reverse();
print(lst);

# OR
lst.sort(reverse=True);     # reverse sort the list

# 4) index(element,start,end): returns the index of a given value else error
print(lst.index(3));
print(lst.index(3,1,4));    # searches within a range

# 5) count(element): returns the count of the occurance of a given value in the list
print(lst.count(2));

#6) copy(): copies list in another variable
# Referencing in PYTHON
l=[1,2,3];
m=l;
m[0]=100;
print(l);   # changes the original list "l" & is not recommended

m=lst.copy();
m[0]=100;
print(lst);

# 7) insert(index,element): inserts an element at a particular index
lst.insert(3,212);

# 8) extend(values): adds another list/tuple,dict/set/etc. to existing list
m=[99,98,97];
lst.extend(m);
print(lst);

# 9) Concatenate two list
m=[1,2,3];
l=[4,5,6];
k=m+l;
print(k);

a=[1,2];
b=[11,12];
c=a+b;
print(c);

# 10) Membership operation
if(12 in b):
    print("Yes");
else:
    print("No");