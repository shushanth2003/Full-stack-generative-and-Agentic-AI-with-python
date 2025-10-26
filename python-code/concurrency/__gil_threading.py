import threading
import time
def brew_chai():
    print(f"Starting to brew chai {threading.current_thread().name}");
    count=0;
    for _ in range(100_00_00):
        count+=1;
    print(f"ending to brew chai {threading.current_thread().name}");

thread1=threading.Thread(target=brew_chai,name="Barista-1");
thread2=threading.Thread(target=brew_chai,name="Barista-2");
start=time.time();
thread1.start();
thread2.start();
thread1.join();
thread2.join();
end=time.time();

print(f"Total time taken {end-start:.2f} seconds")