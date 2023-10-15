# Pickle -> preservation of data, used for implementation of binary protocols
# for serilizing & deseriliazing

# serilizing : python object hierarchy into Byte Stream
# deseriliazing : opp of serilizing

import pickle

# pickle
lst = ['a','b','c'];
file = "sample.pkl";

# open file in binary (imp)
fileobj = open(file, 'wb');
pickle.dump(lst, fileobj);     # dumps: takes variable & return binary string
fileobj.close();
