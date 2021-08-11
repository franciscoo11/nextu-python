import requests
import json
from domain.cryptocurrency import Cryptocurrency


def get_cryptocurrencies():
    headers = {  
        'Accepts': 'application/json',  
        'X-CMC_PRO_API_KEY':  '855cf8de-ff65-416f-8b81-390304275745'
    }
    params = {}
    response =  requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers,params=params)

    jsonResponse = response.json()
    currencies = []
    for currency in jsonResponse["data"]:
        # print(currency["id"], currency["name"], currency["quote"]["USD"]["price"])
        newCurrency = Cryptocurrency(currency["id"],currency["symbol"],currency["name"], currency["quote"]["USD"]["price"])
        currencies.append(newCurrency)
    
    print(currencies)
    return currencies

get_cryptocurrencies()