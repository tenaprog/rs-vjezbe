import asyncio
import aiohttp
import time


async def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main():
    start_time = time.time()
    tasks = [fetch_users() for _ in range(5)]
    results = await asyncio.gather(*tasks)

    names = [user["name"] for user in results[0]]
    emails = [user["email"] for user in results[0]]
    usernames = [user["username"] for user in results[0]]

    print("Imena:", names)
    print("Email adrese:", emails)
    print("Usernames:", usernames)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Vrijeme izvođenja programa: {execution_time:.2f} sekundi")


asyncio.run(main())
