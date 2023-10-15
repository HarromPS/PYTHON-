# Recurison : is a process of defining something in terms of itself
# function calling itself inside the same function

def factorial(n):
    if(n==0 or n==1):
        return 1;
    else:
        return n * factorial(n-1);

x=factorial(3);
print(x);
x=factorial(4);
print(x);

x=factorial(5); # => 120
# 5 * f(5-1)=24
# 4 * f(4-1)=6
# 3 * f(3-1)=2
# 2 * f(2-1)=1
# 1 * f(1-1)=1
# 0 return 1 ^
print(x);

def fibo(n):
    if(n==1 or n==0):
        return 1;
    else:
        return fibo(n-1) + fibo(n-2);

# print fibonacci series upto 10 places
for i in range(1,20):
    print(fibo(i),sep='',end=' ');