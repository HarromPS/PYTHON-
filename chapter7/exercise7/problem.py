# Write a program to clear all the clutter inside of a folder.
# Use os module rename function to rename all the png to beautifully named files like 1.png
# Same for other file formats
'''
ask.png     -> 1.png
askdd.png   -> 2.png
afdfsk.png  -> 3.png
esk.png     -> 4.png
'''

# 1st just go & run problem.py
# 2nd go & run createFiles.py
# 3rd go & run solution.py


# --------------------
# start

import os

# 1st create a folder to solve the problem
if(not os.path.exists("Folder")):
    os.mkdir("Folder");

# create folders for different file formats
folder_list = ['pdfs','imgs','docs'];
for i in range(0,len(folder_list)):
    if(not os.path.exists(f"Folder/{folder_list[i]}")):
        os.mkdir(f"Folder/{folder_list[i]}");

# now run createFiles.py


