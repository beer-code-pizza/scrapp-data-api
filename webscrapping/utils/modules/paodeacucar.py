import json
from pandas import DataFrame
from requests import get, Response

def getItensAndPrices(response: Response) -> DataFrame:
    itens = []
    prices = []
    data  = response.json()
    for content in data["products"]:
        itens.append(content["name"])
        prices.append(content["price"])

    itens_prices = list(zip(itens,prices))
    df = DataFrame(itens_prices, columns=['Item', 'Preco'])
    return df