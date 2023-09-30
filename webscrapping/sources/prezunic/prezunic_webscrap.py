import os
from shutil import rmtree
from pandas import read_csv, concat, DataFrame, notnull
from utils.modules.scrapper import getWithBs4, dataTransformation
from utils.modules.prezunic import getItensAndPrices, getNextUrl

categoryUrls = ["carnes-e-aves","bebida-alcoolica","bebida-nao-alcoolica","congelados",
                "frios-e-laticinios","higiene-e-beleza","hortifruti","limpeza","mercearia"]

source = "prezunic"
path = f"webscrapping/sources/{source}"

df_result = DataFrame({'Item' : [], "Preco": []})

# if os.path.exists(path) and os.path.isdir(path):
#     rmtree(path)
#     os.mkdir(path)
# else:
#     os.mkdir(path)
    
for category in categoryUrls:
    try:
        print("Category: ", category)
        firstUrl = f"https://www.prezunic.com.br/{category}?page="
        getItensAndPrices(getWithBs4(firstUrl+str(1))),source.to_csv(f"{path}/itens_precos_{category}_{source}.csv", header=True, sep = ';', index = False)
        for page in range(2,200):
            next_url = getNextUrl(str(page), category)
            
            print("Sending a GET request to a: ", next_url)
            
            getItensAndPrices(getWithBs4(next_url)).to_csv(f"{path}/itens_precos_{category}_{source}.csv", sep = ';', header = False, index = False, mode='a')
                        
            df = read_csv(f"{path}/itens_precos_{category}_{source}.csv", header=0, delimiter=';', engine='python')
            df_result = concat([df_result,df])
    except:
        pass

df_result = df_result.where(notnull(df_result), None)
df_result.mask(df_result.eq('None')).dropna()
df_result.to_csv(f"{path}/itens_precos_{source}.csv", sep = ';', header = True, index = False, mode='a')

