import requests
import time
import json


# limitando a repetição em 30x
for x in range (30):

    url = 'https://hcomunicaapi.cnj.jus.br/api/v1/comunicacao'

    #requisição API
    requisicao = requests.get(url)
    data = requisicao.json()
    with open("data.json", "a") as outfile:
        json.dump(data, outfile)
    #imprime a numeração da iteração
    print('Loop 10s Iteração nº: ', x)
    #tempo de intervalo da iteração 
    time.sleep(10)