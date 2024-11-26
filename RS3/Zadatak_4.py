import asyncio
import random


async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    return f"Broj {broj} je neparan."


async def main():
    tasks = [
        asyncio.create_task(provjeri_parnost(random.randrange(1, 101))) for i in range(0, 10)
    ]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
