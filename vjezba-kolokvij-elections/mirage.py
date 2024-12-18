from aiohttp import web
import aiohttp
import asyncio
import random


async def glasaj_klijent(session, opcija):
    return await session.post('http://localhost:8080/glasaj', json=opcija)


async def mirage_simulation(broj_zahtjeva):
    opcije = ['plavi', 'crveni', 'krivi']
    tasks = []
    result = {'uspjesni': 0, 'neuspjesni': 0}

    if (broj_zahtjeva < 1):
        broj_zahtjeva = 500

    async with aiohttp.ClientSession() as session:
        for _ in range(0, broj_zahtjeva):
            opcija = random.choice(opcije)
            tasks.append(glasaj_klijent(session, opcija))

        responses = await asyncio.gather(*tasks)

        for r in responses:
            if (r.status == 200):
                result['uspjesni'] += 1
            else:
                result['neuspjesni'] += 1
        return result


async def main():
    print(await mirage_simulation(500))

asyncio.run(main())
