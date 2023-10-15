# Generators: values on-the-fly(on spot)
# returns a sequence of values , a object
# one-by-one generated values as we iterate

# yield keyword - returns a value generated

def fun():
    for i in range(0,10):
        yield i;

gen = fun();
print(next(gen));
print(next(gen));
print(next(gen));
print(next(gen));
