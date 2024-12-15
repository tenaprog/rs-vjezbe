import aiohttp
import asyncio


async def call_micro(url, port):
    async with aiohttp.ClientSession() as session:
        return await session.get(f"{url}:{port}/pozdrav")


async def main():
    # sekvencijalno
    response = await call_micro("http://localhost", 8081)
    print(response)
    response = await call_micro("http://localhost", 8082)
    print(response)

    # konkurentno
    micro1 = asyncio.create_task(call_micro("http://localhost", 8081))
    micro2 = asyncio.create_task(call_micro("http://localhost", 8082))
    response = await asyncio.gather(micro1, micro2)
    print(response)

asyncio.run(main())
