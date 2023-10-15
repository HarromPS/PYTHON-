a= [1,2,3];
b= [4,5,6];
c=zip(a,b);
print(c,type(c));

for x,y in zip(a,b):
    print(x,y);