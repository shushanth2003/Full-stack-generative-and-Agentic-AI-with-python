import asyncio;
from concurrent.futures import ProcessPoolExecutor;

def encrypt(items):
    return f"{items[::-1]}";

async def main():
    loop=asyncio.get_running_loop();
    with ProcessPoolExecutor() as pool:
        result=await loop.run_in_executor(pool,encrypt,"Credit card -1");
        print(f"{result} encrypted sucessfully");

if __name__=="__main__":
    asyncio.run(main());