# 1) dir(): function returns a list all the attributes & methods about any new class object
x = [1,2,3];
print(dir(x));
print(x.count);
print(x.__add__);

# 2) __dir__  : attribute, specially for classes returns a dict representation
class emp:
    def __init__(self,nm,age):
        self.name = nm;
        self.age=age;

obj = emp("mn",12);
print(obj.__dir__);

# 3) help(): function returns the documentation & all descriptions
print(help(obj));