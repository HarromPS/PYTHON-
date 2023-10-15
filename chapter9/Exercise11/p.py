import functools

@functools.lru_cache(maxsize=None)
def fun(a)