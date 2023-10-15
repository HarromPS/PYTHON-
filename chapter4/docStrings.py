'''
Docstrings - helps to understand a function
A functions description. String literal appears right below  a functions name
& is different from comment
'''

def fun(n):
    # if not properly followed, it becomes a comment
    '''This is a docstring just before function defination '''
    print(n*n);
    # This is a comment

fun(2);
print(fun.__doc__);

# PEP-8
# document providing guidelines on how to write Python code efficiently


# The Zen of Python, by Tim Peters
# cmd > python
# >>> import this

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!