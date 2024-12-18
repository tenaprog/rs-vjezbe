from aiohttp import web

votes = {"plavi": 0, "crveni": 0}


async def glasaj(zahtjev):
    glas = await zahtjev.json()
    success = web.json_response({"status": "uspješno glasanje"}, status=200)
    if (glas == "plavi"):
        votes['plavi'] += 1
        return success
    if (glas == "crveni"):
        votes['crveni'] += 1
        return success
    return web.json_response({"status": "nepoznata opcija"}, status=400)


async def trenutni_rezultati(zahtjev):
    return web.json_response(votes, status=400)

app = web.Application()
app.router.add_post('/glasaj', glasaj)
app.router.add_get('/rezultati', trenutni_rezultati)


web.run_app(app, port=8080)
