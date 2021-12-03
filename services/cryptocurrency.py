import requests
import json
from domain.Cryptocurrency import Cryptocurrency

def get_cryptocurrencies():
    key_coinmarket = "855cf8de-ff65-416f-8b81-390304275745"
    headers = {  
        'Accepts': 'application/json',  
        'X-CMC_PRO_API_KEY':  key_coinmarket
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

# REALIZA UN DICT KEY -> NAME, VALUE -> PRECIO EN USD DE COINMARKETCAP.
def get_cryptonamesandprices():
    key_coinmarket = "855cf8de-ff65-416f-8b81-390304275745"
    headers = {  
        'Accepts': 'application/json',  
        'X-CMC_PRO_API_KEY':  key_coinmarket
    }

    data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
    currencies_CMC = {}
   
    for cripto in data["data"]:
        currencies_CMC[cripto["symbol"]] = float(cripto["quote"]["USD"]["price"])
        
    return currencies_CMC

        
def get_price(symbol):
    aux = get_cryptonamesandprices()
    return aux[symbol]

def is_supported_currency(msj):
    return msj in get_cryptonamesandprices()





