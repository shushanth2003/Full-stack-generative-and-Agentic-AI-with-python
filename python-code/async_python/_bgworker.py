import asyncio;
import threading;
import time;
def background_worker():
    while True:
        time.sleep(3);
        print("Logging the health system ❤️")


async def fetch_order():
    await asyncio.sleep(3);
    print("🎁 fetched successfully");

async def main():
    threading.Thread(target=background_worker,daemon=True).start();
    await fetch_order();
    await asyncio.sleep(5);
    


asyncio.run(main());

