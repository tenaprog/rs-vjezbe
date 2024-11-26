import asyncio
import aiohttp


async def get_cat_facts():
    url = "https://catfact.ninja/fact"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def filter_cat_facts(catFactsList):
    return [catFact['fact'] for catFact in catFactsList if 'cat' in catFact['fact'].lower() or 'cats' in catFact['fact'].lower()]


async def main():
    tasks = [get_cat_facts() for _ in range(20)]
    results = await asyncio.gather(*tasks)

    print("Filtrirane činjenice o mačkama:")
    for item in await filter_cat_facts(results):
        print(f"- {item}")

asyncio.run(main())
