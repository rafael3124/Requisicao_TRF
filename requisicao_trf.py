import requests
import time
import json

while True:
    #requisição API
    response=requests.get("/api/v1/comunicacao")
    data=response.json()

    #intervalo de 5 segundos para a próxima requisição
    time.sleep(5)
