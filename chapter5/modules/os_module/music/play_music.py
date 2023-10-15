import os
import shutil

# shutil.copy("A:\College Work\Videos\Audio","A:\VS Codes\Programming\PYTHON\chapter5\modules\os_module\music\list");

lst = os.listdir("list");

# startfile- open file, os.path.join (path, file/folder)- joins various files & folders
os.startfile(os.path.join("list", lst[5]));

