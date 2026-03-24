from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/produto/{id}")
def get_produto(id: int):
    time.sleep(5)
    
def get_produto(id: int):
    produtos = {
        1: {"id": 1, "nome": "Notebook", "preco": 3500},
        2: {"id": 2, "nome": "Mouse", "preco": 150}
    }

    return produtos.get(id, {"erro": "Produto não encontrado"})