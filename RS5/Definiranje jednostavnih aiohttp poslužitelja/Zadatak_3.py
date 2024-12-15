from aiohttp import web

korisnici = [
    {'ime': 'Ivo', 'godine': 25},
    {'ime': 'Ana', 'godine': 17},
    {'ime': 'Marko', 'godine': 19},
    {'ime': 'Maja', 'godine': 16},
    {'ime': 'Iva', 'godine': 22}
]


async def punoljetni_get(request):
    return web.json_response([k for k in korisnici if k['godine'] >= 18])

app = web.Application()
app.router.add_get('/punoljetni', punoljetni_get)

if __name__ == '__main__':
    web.run_app(app, port=8082)
