import os
from requests import get
from shutil import rmtree
from pandas import read_csv, concat, DataFrame, notnull
from modules.paodeacucar import getItensAndPrices

categoryUrls = ["alimentos","beleza-e-perfumaria","bebidas","bebidas-alcoolicas","limpeza","bebes-e-criancas",
                "cuidados-pessoais","suplementos-alimentares","eventos-e-festas","utensilios-e-descartaveis",
                "petshop","floricultura-e-jardim","esporte-e-lazer","cuidados-com-a-saude","moveis-e-decoracao",
                "cama-mesa-e-banho","papelaria","brinquedos-e-jogos","automotivos","casa-e-construcao","celulares-e-smartphones",
                "climatizacao-e-ventilacao","eletrodomesticos","eletroportateis","games-e-videogames","informatica","moda",
                "telefonia-fixa","tv-audio-e-video"]

source = "paodeacucar"
path = f"data/{source}_data"

df_result = DataFrame({'Item' : [], "Preco": [], "Fonte": []})

if os.path.exists(path) and os.path.isdir(path):
    rmtree(path)
    os.mkdir(path)
else:
    os.mkdir(path)

for category in categoryUrls:
    try:
        print("Category: ", category)
        firstUrl = f"https://api.linximpulse.com/engage/search/v3/navigates?apiKey=paodeacucar&origin=https://www.paodeacucar.com&page=1&resultsPerPage=100&multicategory={category}&salesChannel=461&salesChannel=catalogmkp&sortby=relevance"
        response = get(firstUrl)
        getItensAndPrices(response).to_csv(f"{path}/itens_precos_{category}_{source}.csv", header=True, sep = ';', index = False)
        for page in range(2,200):
            fullUrl = f"https://api.linximpulse.com/engage/search/v3/navigates?apiKey=paodeacucar&origin=https://www.paodeacucar.com&page={page}&resultsPerPage=100&multicategory={category}&salesChannel=461&salesChannel=catalogmkp&sortby=relevance"
            print("Sending a GET request to a:", fullUrl)
        
            response = get(fullUrl)
            getItensAndPrices(response).to_csv(f"{path}/itens_precos_{category}_{source}.csv", header=False, sep = ';', index = False, mode = 'a')

            df = read_csv(f"{path}/itens_precos_{category}_{source}.csv", header=0, delimiter=';', engine='python')
            df_result = concat([df_result,df])

    except:
        pass

df_result = df_result.where(notnull(df_result), None)
df_result.to_csv(f"{path}/itens_precos_{source}.csv", sep = ';', header = True, index = False, mode='a')