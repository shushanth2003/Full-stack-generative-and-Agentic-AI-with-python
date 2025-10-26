import threading;
import time;

def take_order():
    for i in range(0,3):
        print(f"Takes a Order {i}");
        time.sleep(2);

def brew_chai():
    for i in range(0,3):
        print(f"Brew a Chai {i}");
        time.sleep(3);

#creating a multithread
order_thread=threading.Thread(target=take_order);
brew_thread=threading.Thread(target=brew_chai);

#start a thread to run in memory
order_thread.start();
brew_thread.start();

#to join the thread
order_thread.join();
brew_thread.join();

print("All done")