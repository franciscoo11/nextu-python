from domain.Cryptobalance import *
import os

storage_folder = "../storage"
script_dir = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(script_dir, storage_folder)

def register_transaction(date,user_id,operation_type,symbol,amount,total_price):
    formate_date = str(date.strftime('%d/%m/%Y %H:%M:%S'))
    archivo=open(f'{folder}/user{user_id}/hystoric_file', 'a+')
    archivo.write(f'{formate_date}|{symbol}|{user_id}|{operation_type}|{str(amount)}|{str(total_price)} \n')
    archivo.close()

def line_balance_register(logged_user,symbol,amount):
    newCriptobalance = Cryptobalance(symbol,amount)
    file=open(f'{folder}/user{logged_user}/balance.txt','a+') 
    file.write(f'{newCriptobalance.symbol}|{newCriptobalance.amount}')
    file.close()

def user_registration(user_id,user_password):
    file=open(f'{folder}/users.txt', 'a+')
    file.write(f'USER:{user_id}|PW:{user_password}\n')
    file.close()
    
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

    with open(f'{folder}/users.txt') as txt:
        if f'USER:{user_id}' in txt.read():
            return True
    return False

def check_id_pass(user_id,user_password):
    file = open(f'{folder}/users.txt', 'r')
    txt = file.read()
    file.close()
    lines = txt.splitlines()
    terms = txt.split("|")
    for line in lines:
        if f'USER:{user_id}|PW:{user_password}' in line:
            return True

    return False

def create_a_folder(user_id):
    if not os.path.exists(f'{folder}/user{user_id}'):
        os.makedirs(f'{folder}/user{user_id}')

def create_filebalance(user_id):
    file = open(f'{folder}/user{user_id}/balance.txt', 'w+')
    file.close()

