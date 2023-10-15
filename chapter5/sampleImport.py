import customModules;
customModules.fun();
print(customModules.variable);

from customModules import fun,variable;
fun();
print(variable);

from customModules import *
#from customModules import * as f : do not works

