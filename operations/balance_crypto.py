from operations.transfer import *
from services.storage import get_currencye_amount
from services.cryptocurrency import get_price
def show_singular_balance(user_id):    
    print('*****                        DESPLEGAR BALANCE POR MONEDA                            *****')
    is_currency_valid = False
    while not is_currency_valid:
        currency = input("Ingrese el simbolo de la criptomoneda que desea conocer su balance: ").upper()
        is_currency_valid = is_supported_currency(currency) 
    cripto_amount = get_currencye_amount(user_id.id,currency)
    cripto_price = get_price(currency)
    print(f'Usted tiene {cripto_amount} de la moneda {currency} y su balance es: {cripto_price * cripto_amount}')