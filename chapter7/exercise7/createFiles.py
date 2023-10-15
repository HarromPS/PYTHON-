import random

# 1st just go & run problem.py
# 2nd go & run createFiles.py
# 3rd go & run solution.py

# --------------------
# start

# create random files inside folders
randChars = ['adefd', 'wewb', 'dec', 'ed', 'wee', 'wef', 'dg', 'h', 'ewi', 'ewej', 'wek', 'wel', 'ewem', 'n', 'o', 'p', 'q', 'rded', 'swe', 'dwt', 'ued', 'ddv', 'eww', 'ewex', 'ywe', 'zwe'];
location = "A:\VS Codes\Programming\PYTHON\chapter7\exercise7\Folder";

folder_list = [['\pdfs','.pdf'],['\imgs','.png'],['\docs','.txt']];
for i in range(0,len(folder_list)):
    for j in range(0,5):
        with open(f"{location+folder_list[i][0]}\{random.choice(randChars)}{folder_list[i][1]}","w"):
            pass

# now run solution.py