import aiohttp
import asyncio


async def glasaj_klijent(opcija):
    async with aiohttp.ClientSession() as session:
        return await session.post('http://localhost:8080/glasaj', json=opcija)


async def rezultati_klijent():
    async with aiohttp.ClientSession() as session:
        return await session.get('http://localhost:8080/rezultati')


async def main():
    response_glasaj_klijent = await glasaj_klijent('plavi')
    response_rezultati_klijent = await rezultati_klijent()
    rezutat = await response_rezultati_klijent.json()
    print(response_glasaj_klijent.status)
    print(rezutat)

asyncio.run(main())
