from datetime import datetime
from os import read, write
from requests.api import get
from services.cryptocurrency import get_price
from services.storage import *

def send(user_id,user_id_destine,amount,symbol):
    now = datetime.now()
    value = float(amount)*float(get_price(symbol))
    date = str(now.strftime("%d de %B de %Y"))
    register_transaction(date,user_id, symbol, amount, get_price(symbol))
    criptobalance = get_criptobalance(user_id,symbol)
    criptobalance.send(amount)
    update_amount_balance(user_id,criptobalance)
    op_receive(user_id_destine, amount, symbol)
    
def op_receive(user_id, amount, symbol):
    now = datetime.now()
    value = float(amount)*float(get_price(symbol))
    date = str(now.strftime("%d de %B de %Y"))
    register_transaction(date,user_id, symbol, amount, get_price(symbol))
    criptobalance = get_criptobalance(user_id,symbol)
    if criptobalance == None:
        criptobalance = Cryptobalance(symbol,amount)
    else:
        criptobalance.receive(amount)
    update_amount_balance(user_id,criptobalance)
        
        
def update_amount_balance(user_id,criptobalance):
    open_file = open(f'{folder}/user{user_id}/balance.txt', 'r')
    new_Content = ""
    founded = False
    
    for line in open_file:
        if criptobalance.symbol in line:
            founded = True
            new_Content += make_balance_reg(criptobalance)
        else:
            new_Content += line

    open_file.close()

    if not founded:
        new_Content += make_balance_reg(criptobalance)

    writing_file = open(f'{folder}/user{user_id}/balance.txt', 'w')

    writing_file.write(new_Content)
    writing_file.close()

    
    
