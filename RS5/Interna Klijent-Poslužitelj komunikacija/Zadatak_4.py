from aiohttp import web

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]


async def proizvod_get(request):
    id = int(request.match_info['id'])
    proizvod = list(filter(lambda p: p['id'] == id, proizvodi))
    if (proizvod):
        return web.json_response(proizvod[0])
    return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)


async def proizvodi_get(request):
    return web.json_response(proizvodi)

app = web.Application()
app.router.add_get('/proizvodi/{id}', proizvod_get)
app.router.add_get('/proizvodi', proizvodi_get)

if __name__ == '__main__':
    web.run_app(app, port=8081)
