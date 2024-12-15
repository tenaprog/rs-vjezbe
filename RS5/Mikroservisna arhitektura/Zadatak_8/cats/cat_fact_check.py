from aiohttp import web


async def facts_post(request):
    body = await request.json()
    response = []
    for fact in body:
        if 'cat'.lower() in fact.lower():
            response.append(fact)
    return web.json_response(response, status=200)

app = web.Application()
app.router.add_post('/facts', facts_post)

if __name__ == '__main__':
    web.run_app(app, port=8087)
