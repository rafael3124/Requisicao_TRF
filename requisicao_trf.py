import requests
import time
import json


# limitando a repetição em 30x
for x in range (30):

    url = 'https://hcomunicaapi.cnj.jus.br/api/v1/comunicacao'

    #Status da requisição
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("Request failed with status code:", response.status_code)


    #requisição API
    requisicao = requests.get(url)
    data = requisicao.json()
    with open("map.json", "a") as outfile:
        json.dump(data, outfile)
    #imprime a numeração da iteração
    print('Loop 10s Iteração nº: ', x)
    #tempo de intervalo da iteração 
    time.sleep(10)
