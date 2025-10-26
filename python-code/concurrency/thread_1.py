import threading;
import time

def boil_milk():
    print("keep milk pan into cloves");
    time.sleep(2);
    print("milk is boiled");

def toasting_bun():
    print("keep bun in cloves pan");
    time.sleep(3);
    print("bun toasted");

thread1=threading.Thread(target=boil_milk);
thread2=threading.Thread(target=toasting_bun);

start=time.time();
thread1.start();
thread2.start();
thread1.join();
thread2.join();
end=time.time();
print(f"session end {end-start:.2f} seconds");