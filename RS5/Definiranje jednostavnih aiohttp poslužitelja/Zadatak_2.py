from aiohttp import web

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]


async def proizvodi_get(request):
    return web.json_response(proizvodi)


async def proizvodi_post(request):
    proizvod = await request.json()
    print(proizvod)
    proizvodi.append(proizvod)
    return web.json_response(proizvodi, status=200)

app = web.Application()
app.router.add_get('/proizvodi', proizvodi_get)
app.router.add_post('/proizvodi', proizvodi_post)

if __name__ == '__main__':
    web.run_app(app, port=8081)
