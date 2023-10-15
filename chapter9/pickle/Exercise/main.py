import pickle

file = open("data.txt",'r');

lst = [];
while(True):
    line = file.readline();
    l = [];
    l.append(line);
    lst.append(l);
    if(not line):
        lst.pop();
        lst.pop();
        break;

file.close();

# pickle
file = "sample.pkl";
fileobj = open(file,'wb');
pickle.dump(lst,fileobj);
fileobj.close();

# depickle
file = "sample.pkl";
fileobj = open(file,'rb');
lst = pickle.load(fileobj);
print(lst);
print(type(lst));