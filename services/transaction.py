from datetime import datetime
from services.cryptocurrency import get_price
from services.storage import register_transaction, balance_register, update_currencye_balance, get_currencye_amount

def send(user_id,user_id_destine,amount,symbol):
    now = datetime.now()
    value = float(amount)*float(get_price(symbol))
    date = str(now.strftime("%d de %B de %Y"))

    # Busco currency balance por simnbolo
    # Actualizo el monto total de la moneda (cryptobalance.amount - amount)
    # Llamamos a register_balance(user,cryptobalance) 

    register_transaction(date,user_id, symbol, amount, get_price(symbol))
    balance_register(symbol,user_id,amount)
    receive(user_id_destine, amount, symbol)
    update_currencye_balance(symbol,user_id,amount)
    
def receive(user_id, amount, symbol):
    now = datetime.now()
    value = float(amount)*float(get_price(symbol))
    date = str(now.strftime("%d de %B de %Y"))
    register_transaction(date,user_id, symbol, amount, get_price(symbol))
    balance_register(symbol,user_id,amount)
    update_currencye_balance(symbol,user_id, amount)


def has_enough_balance(user_id,symbol,amount_trans):
    if get_currencye_amount(user_id,symbol) == None and get_currencye_amount(user_id, symbol).amount < amount_trans:
        return False
    return True



