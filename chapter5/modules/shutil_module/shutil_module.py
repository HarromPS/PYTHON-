# using shutil module copy this main file to two new folders
import shutil

# 1) shutil.copy(src,dest): exact copy of a file, if exists override, matadata not preserved
shutil.copy(f"A:\VS Codes\Programming\PYTHON\chapter5\modules\shutil_module\_file.txt","A:\VS Codes\Programming\PYTHON\chapter5\modules\shutil_module\_file2.txt");

# 2) shutil.copy2(src,dest): exact copy of a file, if exists override, matadata is preserved
shutil.copy2(f"A:\VS Codes\Programming\PYTHON\chapter5\modules\shutil_module\_file.txt","A:\VS Codes\Programming\PYTHON\chapter5\modules\shutil_module\_file2.txt");

# 3) shutil.copytree(src,dst); copies whole folder respectively to new location, if already exists
# merges it
shutil.copytree(f"A:\VS Codes\Programming\PYTHON\chapter5\modules\shutil_module",f"A:\VS Codes\Programming\PYTHON\chapter5\modules\shutil_module\copiedModule");

# 4) shutil.move(src, dst): moves or renames a file
shutil.move(f"A:\VS Codes\Programming\PYTHON\chapter5\modules\shutil_module\_file.txt",f"A:\VS Codes\Programming\PYTHON\chapter5\modules\shutil_module\myFile.txt");

# 5) shutil.rmtree(path): deletes folder recursively
shutil.rmtree(f"A:\VS Codes\Programming\PYTHON\chapter5\modules\shutil_module\copiedModule");