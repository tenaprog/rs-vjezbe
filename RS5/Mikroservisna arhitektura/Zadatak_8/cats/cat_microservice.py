from aiohttp import web
import aiohttp
import asyncio


async def get_fact():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://catfact.ninja/fact') as request:
            response = await request.json()
            return response['fact']


async def cat_get(request):
    amount = int(request.match_info['amount'])
    tasks = []
    for _ in range(0, amount):
        tasks.append(asyncio.create_task(get_fact()))
    facts = await asyncio.gather(*tasks)
    return web.json_response(facts, status=200)

app = web.Application()
app.router.add_get('/cat/{amount}', cat_get)

if __name__ == '__main__':
    web.run_app(app, port=8086)
