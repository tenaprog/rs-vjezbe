from aiohttp import web
from aiohttp.web import AppRunner
import asyncio
import aiohttp

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

narudzbe = []


async def proizvod_get(request):
    id = int(request.match_info['id'])
    proizvod = list(filter(lambda p: p['id'] == id, proizvodi))
    if (proizvod):
        return web.json_response(proizvod[0])
    return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)


async def proizvodi_get(request):
    return web.json_response(proizvodi)


async def narudzbe_post(request):
    narudzba = await request.json()
    proizvod = list(
        filter(lambda p: p['id'] == narudzba['proizvod_id'], proizvodi))
    if (proizvod):
        narudzbe.append(narudzba)
        return web.json_response(narudzbe)
    return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

app = web.Application()
app.router.add_get('/proizvodi/{id}', proizvod_get)
app.router.add_get('/proizvodi', proizvodi_get)
app.router.add_post('/narudzbe', narudzbe_post)


async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()


async def main():
    await start_server()

    async with aiohttp.ClientSession() as session:
        response = await session.get('http://localhost:8081/proizvodi')
        print(await response.json())

        response = await session.get('http://localhost:8081/proizvodi/3')
        print(await response.json())

        response = await session.get('http://localhost:8081/proizvodi/9')
        print(await response.json())

        response = await session.post('http://localhost:8081/narudzbe', json={"proizvod_id": 3, "kolicina": 2})
        print(await response.json())

if __name__ == '__main__':
    asyncio.run(main())
