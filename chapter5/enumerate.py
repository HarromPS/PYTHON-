# To loop over a sequence like list, tuple, dict & get index, val

marks = [1,2,3,4];

# normal way
i = 0;
for val in marks:
    if(i>1):
        print(val);
    i=i+1;

# enumerate
for (index,value) in enumerate(marks):
    if(i>1):
        print(index,value);

# changing starting index
for (i,val) in enumerate(marks,start=1):
    print(val);

# virtual environment
# -> a tool to isolate sepcific Python environment on the same machine , allows to work on different
# dependencies & packages without conflict, useful when packages or versions of different
# projects are not compatible with each other

# create a new envt
# python -m venv myenv (name of env)

# activate envt.
# myenv\Scripts\activate.bat
# any package fom pip will get installed in myenv & not in global envt without affecting global packages & any program will use this virtual envt to run

import pandas as pd
print(pd.__version__);

# requirement.txt : list of all dependencies, packages & their versions a project needed
# file is used as a portable & used to install all required packages

# create a file
# pip freeze > requirements.txt

# install packages
# pip install -r requirements.txt