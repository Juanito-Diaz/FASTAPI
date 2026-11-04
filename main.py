from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    tittle = "Aprendiendo FASTAPI",
    description = "Una API en los primeros pasos",
    version = "0.0.1",
)

@app.get("/" , tags=["Inicio"])
def read_root():
    return HTMLResponse(' <h2>Hola Mundo</h2> ')








"""
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
"""
