# function caching & Momoization:
# caching values so that it can be retrived without repeating computations
# saves time & space

import functools
import time

# lru decorator
@functools.lru_cache(maxsize=None)
def fun(val):
    time.sleep(3);
    return (val);

# 3 sec for each
print(fun(10));
print(fun(11));
print(fun(12));

# quickly
print(fun(10));
print(fun(11));
print(fun(12));