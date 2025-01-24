from fastapi import FastAPI
from routers.filmovi import router_filmovi

app = FastAPI()

app.include_router(router_filmovi)


@app.get("/")
def read_root():
    return {"message": "App radi."}
