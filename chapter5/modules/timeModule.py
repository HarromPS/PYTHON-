# Time module: set of functions related to time related functions
import time

# 1) .time(): returns a floating point number represents seconds since 1st jan 1970(epoch)
init = time.time();
print(init);
for i in range(0,1000):
    print(i,end=' ');
print("\n",time.time()-init);

# 2) .sleep(): delays in execution
print(10);
time.sleep(3);      # 3 seconds
print(11);

# 3) .strftime(): string format time into a specified format
t = time.time();
f = time.strftime("%Y-%m-%d %H:%M:%S",t);     # (format,time)
print(f);