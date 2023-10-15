# Multi Threading -> ||al working (download 10 files parallely)
# Achieving Concurrecy
import threading
import time

def fun(a):
    time.sleep(3);
    print(a);

# time1 = time.perf_counter();
# runs in a procedural manner
# fun(1);
# fun(2);
# fun(3);

time1 = time.perf_counter();
# same with threads
# create thread & provide them tasks
t1=threading.Thread(target = fun,args= [1]);
t2=threading.Thread(target = fun,args= [2]);
t3=threading.Thread(target = fun,args= [3]);

# only starts the threading as thrown in background
t1.start();
t2.start();
t3.start();

# join the threads
t1.join();
t2.join();  # waits until t1 ends
t3.join();  # waits until t2 ends

# calculating time
time2 = time.perf_counter();
print(time2-time1);