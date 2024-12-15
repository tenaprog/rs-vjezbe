from aiohttp import web


async def umnozak_post(request):
    if (request.content_length < 3):
        return web.json_response({"message": "Neispravno tjelo zahtjeva"}, status=400)
    data = await request.json()
    umnozak = 1
    for i in data:
        umnozak = umnozak*i
    return web.json_response({"umnozak": umnozak}, status=200)

app = web.Application()
app.router.add_post('/umnozak', umnozak_post)

if __name__ == '__main__':
    web.run_app(app, port=8084)
