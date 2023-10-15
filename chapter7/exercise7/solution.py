# 1st just go & run problem.py
# 2nd go & run createFiles.py
# 3rd go & run solution.py


'''
ask.png     -> 1.png
askdd.png   -> 2.png
afdfsk.png  -> 3.png
esk.png     -> 4.png
'''

# --------------------
# start


import os

folder_list = [['pdfs','.pdf'],['imgs','.png'],['docs','.txt']];
for i in range(0,len(folder_list)):
    if(os.path.exists(f"Folder/{folder_list[i][0]}")):
        for j in range(0,len(os.listdir(f"Folder\{folder_list[i][0]}"))):
            lst = os.listdir(f"Folder\{folder_list[i][0]}");
            os.rename(f"Folder/{folder_list[i][0]}/{lst[j]}",f"Folder/{folder_list[i][0]}/{j+1}{folder_list[i][1]}");