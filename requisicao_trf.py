import requests
import time
import json


#repetição
while True:

    url = 'https://hcomunicaapi.cnj.jus.br/api/v1/comunicacao'

    #requisição API
    requisicao = requests.get(url)
    data = requisicao.json()
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)
    print('Loop 10s', flush=True)
    time.sleep(10)