import time;
import threading;

counter=0;
locks=threading.Lock();

def increment():
    global counter;
    for _ in range(100000):
        with locks:
            counter+=1;

start=time.time();
threads=[threading.Thread(target=increment) for _ in range(10)];
[t.start() for t in threads];
[t.join() for t in threads];
end=time.time();

print(f"final counter {counter}");
print(f"sessions end {end-start:.2f} seconds");
