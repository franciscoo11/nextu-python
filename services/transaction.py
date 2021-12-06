from datetime import datetime
from os import read, write
from requests.api import get
from services.cryptocurrency import get_price
from services.storage import *

transfer_type = "TRANSFER"
recept_type = "RECEIVE"

def send(transaction):
    transaction.total_price = float(transaction.amount)*float(get_price(transaction.symbol))
    register_transaction(transaction.date,transaction.origin_id,transfer_type,transaction.symbol,transaction.amount,transaction.total_price)
    criptobalance = get_criptobalance(transaction.origin_id,transaction.symbol)
    criptobalance.send(transaction.amount)
    update_amount_balance(transaction.origin_id,criptobalance)

    
def receive(transaction):
    transaction.total_price = float(transaction.amount)*float(get_price(transaction.symbol))
    register_transaction(transaction.date,transaction.destination_id,recept_type,transaction.symbol,transaction.amount,transaction.total_price)
    criptobalance = get_criptobalance(transaction.destination_id,transaction.symbol)
    if criptobalance == None:
        criptobalance = Cryptobalance(transaction.symbol,transaction.amount)
    else:
        criptobalance.receive(transaction.amount)
    update_amount_balance(transaction.destination_id,criptobalance)
        
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

    
def new_transaction(transaction):
    send(transaction)
    receive(transaction)