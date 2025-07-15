from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bookSearcher import bookSearch
import logging


# Configuración de logging
logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.INFO)

logger.info("starting app")

class Query(BaseModel):
    query: str

app = FastAPI()

def booksearch(q: Query):
    logger.info(f"Received request: {q.query.strip()}")
    texto = q.query.strip()
    logger.info(f"\n\n{texto}\n\n")
    if not texto:
        logger.error("Parametro vacio")
        raise HTTPException(status_code=400, detail="El parámetro 'query' no puede estar vacío")
    resultados = bookSearch(texto)
    logger.info(f"Procesado")
    return {
        "query": texto,
        "count": len(resultados),
        "books": resultados
    }

@app.get("/")
async def healthcheck():
    return None

@app.post("/search")
async def search(q: Query):
    return booksearch(q)

@app.get("/search")
async def healthcheck(q: Query):
    return booksearch(q)

