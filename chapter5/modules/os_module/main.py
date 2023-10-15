# OS module : performs functions of our operating system
# can automate OS manual functions
# e.g creating files in every folder

import os

# check if path exists
if(not os.path.exists("Data")):
    # make directory then
    os.mkdir("Data");

# make bulk folders
for i in range(1,11):
    if(not os.path.exists(f"Data/day{i}")):
        os.mkdir(f"Data/day{i}");

# make files in folder
for i in range(1,11):
    if(not os.path.exists(f"Data/day{i}/demo.py")):
        os.mkdir(f"Data/day{i}/demo.py");
    os.rename(f"Data/day{i}/demo.py",f"Data/day{i}/Demo");

# os.rename("remame.py","rename.py");