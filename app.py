from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bookSearcher import bookSearch

class Query(BaseModel):
    query: str

app = FastAPI()

@app.post("/search")
async def search(q: Query):
    texto = q.query.strip()
    if not texto:
        raise HTTPException(status_code=400, detail="El parámetro 'query' no puede estar vacío")
    resultados = bookSearch(texto)
    return {
        "query": texto,
        "count": len(resultados),
        "books": resultados
    }
