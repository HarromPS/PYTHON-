# import: process of loading code from into current script.
# allows to use any function and variable in a module as well as additional module

import pandas;
# pandas.read_csv();  # read csv as a data frame when passed with a argument
# pandas.read_xml();

# and any code for required for pandas is also imported through pandas e.g Datutils

import math;

print(math.sqrt(4));
print(math.floor(3.23));
print(math.ceil(3.23));

# from keyword : used to import a particular function from a module
from math import sqrt, floor;   # we can directly use the functions
print(sqrt(25));

# import everything *
from math import *;  # not recommended as it creates confusion
print(ceil(3));

# as keyword: alias for a module or a short name
from math import ceil as cl;
print(cl(2.23));

# dir function : if we don't know asbout a module dir function helps to view the names
# of the functions and variable names
import math;
print(dir(math),type(dir(math)),type(math));
print(math.nan,type(math.nan));

