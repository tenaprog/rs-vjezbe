import aiohttp
import asyncio


async def call_micro(url, body):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=body) as request:
            response = await request.json()
            return response


async def main():
    micro1 = asyncio.create_task(call_micro(
        "http://localhost:8083/zbroj", [2, 5, 8, 9, 15]))
    micro2 = asyncio.create_task(call_micro(
        "http://localhost:8084/umnozak", [3, 6, 1, 7]))

    response1, response2 = await asyncio.gather(micro1, micro2)

    response = await call_micro("http://localhost:8085/kolicnik", [
        response2.get("umnozak"), response1.get("zbroj")
    ])
    print(response)

asyncio.run(main())
