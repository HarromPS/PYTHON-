# Walrus operator - added in Python 3.8
# assigns values in an expression
#Syntax: (:=)

# a= True;
# print(a=False);   # error

a= True;
print(a:=False);

lst = [];
while(True):
    food=input("Enter: ");
    if(food=="quit"):
        break;
    lst.append(food);
print(lst);

lst=[];

# simple way
while(food:=input("Enter: ")) !="quit":
    lst.append(food);
print(lst);