import asyncio;

async def brew_chai(name):
    print(f"chai is started to brewing it to make special {name}");
    await asyncio.sleep(2);
    print(f"chai is ended to brewing it to make special {name}");

async def main():
    await asyncio.gather(
        brew_chai("ginger"),
        brew_chai("masala"),
        brew_chai("cinnademon")
    );

asyncio.run(main());