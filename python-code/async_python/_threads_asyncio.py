import asyncio;
from concurrent.futures import ThreadPoolExecutor;
import time;
#checking the stock information
def check_stock(items):
    print(f"I need to find {items} items in stock");
    time.sleep(3);
    return f"I finded the {items} item in stock";

#linking in thread
async def main():
    with ThreadPoolExecutor() as pool:
        loop=asyncio.get_running_loop();
        result=await loop.run_in_executor(pool,check_stock,"masala");
        print(result);

asyncio.run(main());