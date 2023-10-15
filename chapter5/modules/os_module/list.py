import os

# listing all the folders
folders = os.listdir("Data");

# folders inside folders
i=1;
for dirs in folders:
    print(dirs,sep="",end=" ");
    print(os.listdir(f"Data/day{i}"),sep="",end=" ");
    print(os.listdir(f"Data/day{i}/Demo"));
    i=i+1;