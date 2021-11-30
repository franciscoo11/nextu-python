from datetime import datetime
from domain.Cryptobalance import *
import os
transactions_file = "transactions.txt"
balance_file = "balance.txt"
storage_folder = "../storage"
historic_file = "transactions.txt"
script_dir = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(script_dir, storage_folder)


def register_transaction(date,user_id,currency,amount,price):
    archivo=open(f'{folder}/user{user_id}/+historic_file', 'a+')
    archivo.write(f'{date}|{currency}|{user_id}|{str(amount)}|{str(price)}')
    archivo.close()

def balance_register(logged_user,cryptobalance):
    archivo=open(f'{folder}/user{logged_user}/balance.txt','a+')
    if cryptobalance.symbol in archivo:
        line =    
    archivo.write(f'{moneda}|{logged_user}|{str(amount)}|')
    archivo.close()

    
def get_currencies_balance(user_id, symbol):
    balance_file = open(f'{folder}/user{user_id}/balance.txt', 'r')
    txt = balance_file.read()
    balance_file.close()
    criptos_balance = {}
    separators = txt.split("|") 
    for line in txt.splitlines():
        newCryptobalance = parse_reg(line)
        criptos_balance[newCryptobalance.symbol] = newCryptobalance

    return criptos_balance

def get_currencye_amount(user_id,symbol):
    balance = get_currencies_balance(user_id,symbol)
    if symbol in balance:
        return balance[symbol].amount

    return 0

def update_currencye_balance(criptobalance,user_id,amount):
    reading_file = open(f'{folder}/user{user_id}/balance.txt', 'r')
    new_content = ""
    for line in reading_file:
        if criptobalance in line:
            new_content += make_balance_reg



    
    
    
    
    
    
    lines = balance_file.readlines()
    for line in lines:
        if criptobalance in line:
            newCryptobalance = parse_reg(line)
            line.replace(f'{newCryptobalance.symbol}|{newCryptobalance.amount - amount}')
        

def parse_reg(register):
    separator = register.split("|")
    return Cryptobalance(separator[0],float(separator[1]))

def make_balance_reg(criptobalance):
    return (f'{criptobalance.symbol}|{criptobalance.amount}')
    

    
