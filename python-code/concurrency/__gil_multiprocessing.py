from multiprocessing import Process;
import time
def brew_chai():
    print("starting process");
    count=0;
    for _ in range(1000_000):
        count+=1;
    print("ending process");

if __name__=="__main__":
    process1=Process(target=brew_chai);
    process2=Process(target=brew_chai);
    start=time.time();
    process1.start();
    process2.start();
    process1.join();
    process2.join();
    end=time.time();
    print(f"Session end {end-start:.2f}");