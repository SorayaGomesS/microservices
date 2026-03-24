from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/pedido/{id}")
def get_pedido(id: int):
    try:
        response = requests.get(f"http://service1:8000/produto/{id}", timeout=2)

        produto = response.json()

        return {
            "pedido_id": id,
            "produto": produto
        }

    except requests.exceptions.ConnectionError:
        return {"erro": "Serviço 1 fora do ar"}

    except requests.exceptions.Timeout:
        return {"erro": "Serviço demorou demais"}