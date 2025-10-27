import threading;
import time;
 
def monitoring_tea():
    while True:
        print("Monitoring System 👁️");
        time.sleep(3);

t=threading.Thread(target=monitoring_tea,daemon=True);
t.start();

print("All Done Successfully 👍")

time.sleep(10);