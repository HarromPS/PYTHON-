# Operation on Tuple
# 1) tuple slicing
tple = (1,2,3,4,5,5,55,5,6,7,8,9);
tp=tple[1:4];
print(tp,type(tp));

# New Tuple Indirectly
# 2) As tuples are immutable, copy to another variable & convert to
# List, do the modification & reconvert to tuple
lst = list(tple);
lst.append(99);
lst.append(98);
lst.append(97);
tple = tuple(lst);
print(tple);

# New Tuple Directly
# 3) Concatenate two tuple to new tuple
t1=(1,2,3);
t2=(4,5,6);
t3 = t1 + t2;
print(t3);

# 4) count(element): returns count of no. of occurances of a element
print(tple.count(5));
print(tple.count(125)); # else 0

# 5) index(element, start, end): returns the index of an element, else error
print(tple.index(5));
print(tple.index(5,3,7)); # searches in a range

# All methods can be done by converting tuple to a list