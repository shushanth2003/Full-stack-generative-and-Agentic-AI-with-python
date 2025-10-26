import asyncio
import aiohttp;

async def fetch_url(session,url):
    async with session.get(url) as res:
        print(f"{url} session status is ok {res.status}")
        print("Content-type:", res.headers['content-type'])
        html = await res.text()
        print("Body:", html[:15], "...")


async def main():
    async with aiohttp.ClientSession() as session:
        urls=["https://pypi.org/project/aiohttp/"]*3;
        tasks=[fetch_url(session,url) for url in urls];
        await asyncio.gather(*tasks);

asyncio.run(main());