from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Servicio Producto")

productos: Dict[int, Dict] = {}


# clase producto
class Producto(BaseModel):
    id: int
    name: str
    descripcion: str


# crear producto
@app.post("/productos/", response_model=Producto)
def crear_producto(producto: Producto):
    if producto.id in productos:
        raise HTTPException(status_code=400, detail="producto existe")
    productos[producto.id] = producto.dict()
    return producto


# obteber producto por id
@app.get("/productos/{id}", response_model=Producto)
def buscar_producto(id: int):
    if id not in productos:
        raise HTTPException(status_code=404, detail="producto no encontrado")
    return productos[id]


# actualizar producto
@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    if id not in productos:
        raise HTTPException(status_code=404, detail="producto no encontrado")
    del productos[id]
    return {"detalle": "producto eliminado"}


# verifica la salud del servicio
@app.get("/health")
def health():
    return {"status": "ok"}
