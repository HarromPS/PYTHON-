# Multi Threading -> ||al working (download 10 files parallely)
# Achieving Concurrecy
import threading
import time

# current.futures -> module (give function & get result)
from concurrent.futures import ThreadPoolExecutor

def fun(a):
    time.sleep(3);
    print(f"sleep for {a} secs");

# time1 = time.perf_counter();
# runs in a procedural manner
# fun(1);
# fun(2);
# fun(3);

def main():
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

# makes the above easy
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(fun,11);
        # future2 = executor.submit(fun,12);
        # future3 = executor.submit(fun,31);
        # print(future1);
        # print(future2);
        # print(future3);

        # OR use map function
        args=[11,22,33,44];
        result = executor.map(fun,args);
        for res in result:
            print(res);



poolingDemo();