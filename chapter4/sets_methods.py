A = {1,2,5,6};
B = {3,6,7};

# 1) union()
s1=set(A);
s2=set(B);
s3 = s1.union(s2);  # do not updates s1 & s2, instead returns a new set
print(s3);

# 2) update() - updates the calling set
s1.update(s2);
print(s1);

s1.clear();
s2.clear();
s1.update(A);
s2.update(B);

# 3) intersection() - common elements
s3 = s1.intersection(s2);
print(s3);

# 4) intersection_update() - common elements + update calling se
s1.intersection_update(s2);
print(s1);
s1.clear();
s2.clear();
s1.update(A);
s2.update(B);
s3.clear();

# 5) symmetric_difference() - (A-B) U (B-A) OR (AUB) - (ANB);
s3 = s1.symmetric_difference(s2);
print(s3);

# 6) symmetric_difference_update()
s1.symmetric_difference_update(s2);
print(s1);
s1.clear();
s2.clear();
s1.update(A);
s2.update(B);
s3.clear();

# 7) difference - (A-B)
s3 = s1.difference(s2);
print(s3);

# 8) difference_update()
s1.difference_update(s2);
print(s1);
s1.clear();
s2.clear();
s1.update(A);
s2.update(B);
s3.clear();

# 9) isdisjoint() - returns if no intersection of sets
x=s1.isdisjoint(s2);
print(x);

# 10) issuperset() - returns true if a set is superset of other
x=s1.issuperset(s2);
print(x);

# 11) issubset() - returns true if a set is a subset of other
x=s2.issubset(s1);
print(x);

s2.clear();
s2.update(B);
# 12) add() - add a new element in set
s2.add(12);
print(s2);

# 13) update() - adds multiple elements
s2.update({"True","False"});
print(s2);

# 14) remove() -deletes a elements
# gives a error of try to delete non-present element
s2.remove(12);
print(s2);

# 15) discard() - deletes a elements
# do not gives error
s2.discard(6);
print(s2);

# 16) pop() - removes last element & return deleted element
x=s2.pop();
print(x);

# 17) del - not a method, is a keyword deletes set
del s2;
# print(s2); # else gives a NameError

# 18) clear() - clears the set
s1.clear()
if len(s1)==0:
    print("Empty");
else:
    print("Full");

# 19) check if a element is present
if 1 in A:
    print("Present");
else:
    print("Absent");
