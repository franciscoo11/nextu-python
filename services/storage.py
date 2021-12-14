from datetime import datetime
from domain.Cryptobalance import *
import os
storage_folder = "../storage"
script_dir = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(script_dir, storage_folder)


def register_transaction(date,user_id,operation_type,symbol,amount,total_price):
    formate_date = str(date.strftime("%d de %B de %Y"))
    archivo=open(f'{folder}/user{user_id}/hystoric_file', 'a+')
    archivo.write(f'{formate_date}|{symbol}|{user_id}|{operation_type}|{str(amount)}|{str(total_price)} \n')
    archivo.close()

def line_balance_register(logged_user,symbol,amount):
    newCriptobalance = Cryptobalance(symbol,amount)
    archivo=open(f'{folder}/user{logged_user}/balance.txt','a+') 
    archivo.write(f'{newCriptobalance.symbol}|{newCriptobalance.amount}')
    archivo.close()

def user_register(user_id,user_password):
    archivo=open(f'{folder}/users.txt', 'a+')
    archivo.write(f'{user_id}|{user_password} \n')
    archivo.close()
    
def get_currencies_balance(user_id, symbol):
    balance_file = open(f'{folder}/user{user_id}/balance.txt', 'r')
    txt = balance_file.read()
    file_size = os.path.getsize(f'{folder}/user{user_id}/balance.txt')
    if file_size == 0:
        return {}
    balance_file.close()
    criptos_balance = {}
    for line in txt.splitlines():
        newCryptobalance = parse_reg(line)
        criptos_balance[newCryptobalance.symbol] = newCryptobalance

    return criptos_balance

def get_currencye_amount(user_id,symbol):
    balance = get_currencies_balance(user_id,symbol)
    if symbol in balance:
        return balance[symbol].amount

    return 0


def parse_reg(register):
    separator = register.split("|")
    return Cryptobalance(separator[0],float(separator[1]))

def make_balance_reg(criptobalance):
    return (f'{criptobalance.symbol}|{criptobalance.amount} \n')
    
def get_obj(symbol,amount):
    newCriptobalance = Cryptobalance(symbol,amount)
    return newCriptobalance
    
def get_criptobalance(user_id,symbol):
    balance = get_currencies_balance(user_id,symbol)
    if symbol in balance:
        return balance[symbol]
    else:
        return None

def last_userid():
    file = open(f'{folder}/users.txt', 'r')
    txt = file.read()
    file.close()
    lines = txt.splitlines()
    terms = txt.split("|")
    for line in lines:
        termino = line.split("|")
        x = termino[0]
    return x 
    
def check_id_exist(user_id):
    users_file = open(f'{folder}/users.txt', 'r')
    found = False
    for line in users_file:
        if user_id in line:
            found = True
            break
    return found

def check_id_pass(user_id,user_password):
    file = open(f'{folder}/users.txt', 'r')
    txt = file.read()
    file.close()
    lines = txt.splitlines()
    terms = txt.split("|")
    for line in lines:
        if user_id + '|' + user_password in line:
            return True

    return False