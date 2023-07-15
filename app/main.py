from fastapi import FastAPI

app = FastAPI(
    title="OD Factoring, Facturas Disponibles",
    description="Open Data - Servicio para obtener facturas disponible",
)


@app.get("/")
async def root():
    return {"message": "melo"}
