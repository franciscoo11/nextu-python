from datetime import datetime
from domain.Cryptobalance import *

transactions_file = "transactions.txt"
balance_file = "balance.txt"
storage_folder = "../storage"
historic_file = "transactions.txt"

def register_transaction(date,user_id,currency,amount,price):
    archivo=open(storage_folder+"/"+user_id+"/"+historic_file,'a+')
    archivo.write(date+"|"+currency+"|" + user_id + "|" + str(amount) + "|" + str(price) + "\n")
    archivo.close()

def balance_register(moneda,logged_user,amount):
    archivo=open(storage_folder+"/"+logged_user+"/"+'balance.txt','a+')
    archivo.write(moneda+ "|" + logged_user + "|" + str(amount) + "|" + "\n")
    archivo.close()

    
def get_currencies_balance(user_id, symbol):
    balance_file = open(storage_folder+"/"+user_id+"/"+"balance.txt", 'r')
    txt = balance_file.read()
    balance_file.close()
    criptos_balance = []
    separators = txt.split("|") 
    for line in txt.splitlines():
        newCryptobalance = parse_reg(line)
        criptos_balance.append(newCryptobalance)

    return criptos_balance

def get_currencye_amount(user_id,symbol):
    for cryptobalance in get_currencies_balance(user_id, symbol):
        if cryptobalance.symbol == symbol:
            return cryptobalance

    return None

def update_currencye_balance(criptobalance,user_id,amount):
    balance_file = open(storage_folder+"/"+user_id+"/"+"balance.txt", 'w')
    lines = balance_file.readlines()
    for line in lines:
        if criptobalance in line:
            newCryptobalance = parse_reg(line)
            line.replace(f'{newCryptobalance.symbol} "|" {newCryptobalance.amount - amount} \n')
        

def parse_reg(register):
    separator = register.split("|")
    return Cryptobalance(separator[0],separator[1])
    

    
