import asyncio


async def fetch_data():
    print('Dohvaćam podatke...')
    data = [i for i in range(1, 11)]
    await asyncio.sleep(3)
    print('Podaci dohvaćeni.')
    return data


async def main():
    data = await fetch_data()
    print(f'Podaci: {data}')

asyncio.run(main())
