import threading;
import time;
import requests;

def download(url):
    print(f"Downloading url {url}");
    response=requests.get(url);
    print(f"Downloaded url successfully {response.content} bytes");

urls=[
    "https://httpbin.org/image/svg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/jpeg"
];

threads=[];
start=time.time();

for url in urls:
    t1=threading.Thread(target=download,args=(url,));
    t1.start();
    threads.append(t1);

for t in threads:
    t.join();

end=time.time();

print(f"session ends {end-start:.2f}");