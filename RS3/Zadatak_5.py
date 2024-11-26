import asyncio

podatci = [
    {
        'prezime': 'horvat',
        'broj_kartice': '123456789',
        'CVV': '123'
    },
    {
        'prezime': 'peric',
        'broj_kartice': '234567891',
        'CVV': '231'
    },
    {
        'prezime': 'anic',
        'broj_kartice': '345678912',
        'CVV': '312'
    },
]


async def secure_data(podatak):
    await asyncio.sleep(3)
    return {
        'prezime': podatak['prezime'],
        'broj_kartice': hash(podatak['broj_kartice']),
        'CVV': hash(podatak['CVV'])
    }


async def main():
    tasks = [asyncio.create_task(secure_data(podatak)) for podatak in podatci]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
