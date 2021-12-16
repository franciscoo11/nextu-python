import requests
import json
from domain.Cryptocurrency import Cryptocurrency
import sys

def get_cryptonamesandprices():
    key_coinmarket = "855cf8de-ff65-416f-8b81-390304275745"
    headers = {  
        'Accepts': 'application/json',  
        'X-CMC_PRO_API_KEY':  key_coinmarket
    }
    try:
        data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
    except:
        print("Ha ocurrido un error en establecer la conexion de red.")
        sys.exit()
    currencies_CMC = {}
   
    for cripto in data["data"]:
        currencies_CMC[cripto["symbol"]] = float(cripto["quote"]["USD"]["price"])
        
    return currencies_CMC

        
def get_price(symbol):
    aux = get_cryptonamesandprices()
    return aux[symbol]

def is_supported_currency(crypto):
    return crypto in get_cryptonamesandprices()





