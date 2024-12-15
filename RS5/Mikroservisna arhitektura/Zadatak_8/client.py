import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        response1 = await session.get("http://localhost:8086/cat/15")
        facts = await response1.json()
        response2 = await session.post("http://localhost:8087/facts", json=facts)
        filtered = await response2.json()
        print(filtered)


asyncio.run(main())
