from aiohttp import web


async def zbroj_post(request):
    if (request.content_length < 3):
        return web.json_response({"message": "Neispravno tjelo zahtjeva"}, status=400)
    data = await request.json()
    return web.json_response({"zbroj": sum(data)}, status=200)

app = web.Application()
app.router.add_post('/zbroj', zbroj_post)

if __name__ == '__main__':
    web.run_app(app, port=8083)
