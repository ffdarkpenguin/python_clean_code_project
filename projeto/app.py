from fastapi import FastAPI

from projeto.roteadores import usuario


app = FastAPI()

app.include_router(usuario.roteador)
