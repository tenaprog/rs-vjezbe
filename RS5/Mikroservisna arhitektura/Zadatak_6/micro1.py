from aiohttp import web
import asyncio


async def pozdrav_get(request):
    await asyncio.sleep(3)
    return web.json_response({"message": "Pozdrav nakon 3 sekunde"}, status=200)

app = web.Application()
app.router.add_get('/pozdrav', pozdrav_get)

if __name__ == '__main__':
    web.run_app(app, port=8081)
