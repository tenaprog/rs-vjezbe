from aiohttp import web
import hashlib

korisnici = [
    # lozinka = "lozinka123"
    {"korisnicko_ime": "admin",
        "lozinka_hash": "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b"},
    # lozinka = "markoKralj123"
    {"korisnicko_ime": "markoMaric",
        "lozinka_hash": "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa"},
    # lozinka = "lllllllllllozinka_123"
    {"korisnicko_ime": "ivanHorvat",
        "lozinka_hash": "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302"},
    # lozinka = "blablabla"
    {"korisnicko_ime": "Nada000",
        "lozinka_hash": "492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d"}
]


def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


async def register(request):
    data = await request.json()
    korisnicko_ime = data.get("korisnicko_ime")
    lozinka = data.get("lozinka")

    lozinka_hash = hash_data(lozinka)
    korisnici.append(
        {"korisnicko_ime": korisnicko_ime,
         "lozinka_hash": lozinka_hash}
    )
    return web.json_response({"message": "Registracija uspješna."}, status=201)


async def login(request):
    data = await request.json()
    korisnicko_ime = data.get("korisnicko_ime")
    lozinka = data.get("lozinka")

    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == korisnicko_ime:
            if korisnik["lozinka_hash"] == hash_data(lozinka):
                return web.json_response({
                    "message": "Prijava uspješna.",
                    "autorizacija": True  # Add this field
                }, status=200)
            else:
                return web.json_response({"error": "Neispravna lozinka."}, status=401)

    return web.json_response({"error": "Korisnik ne postoji."}, status=404)

app = web.Application()
app.router.add_post("/register", register)
app.router.add_post("/login", login)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=9000)
