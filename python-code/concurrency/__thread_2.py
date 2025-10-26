import threading;
import time;

def prepare_chai(_type,wait_time):
    print(f"special {_type} tea is preparing");
    time.sleep(wait_time);
    print(f"{_type} tea is prepared");

t1=threading.Thread(target=prepare_chai,args=("Masala",2));
t2=threading.Thread(target=prepare_chai,args=("Ginger",3));

start=time.time();
t1.start();
t2.start();
t1.join();
t2.join();
end=time.time();

print(f"session ends {end-start:.2f} seconds")