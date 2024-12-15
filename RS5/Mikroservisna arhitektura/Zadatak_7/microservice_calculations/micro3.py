from aiohttp import web


async def kolicnik_post(request):
    data = await request.json()
    if (data[1] == 0):
        return web.json_response({"error": "Nije dozvoljeno dijeliti sa nulom"}, status=400)
    kolicnik = data[0]/data[1]
    return web.json_response({"kolicnik": kolicnik}, status=200)

app = web.Application()
app.router.add_post('/kolicnik', kolicnik_post)

if __name__ == '__main__':
    web.run_app(app, port=8085)
