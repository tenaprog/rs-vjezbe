from aiohttp import web

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]


async def proizvodi_handler(request):
    return web.json_response(proizvodi)

app = web.Application()
app.router.add_get('/proizvodi', proizvodi_handler)

if __name__ == '__main__':
    web.run_app(app, port=8081)
