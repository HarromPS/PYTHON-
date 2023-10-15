import pickle

# depickle
file2 = "sample.pkl";
with open(file2, 'rb') as f:
    lst = pickle.load(f);
    print(lst);