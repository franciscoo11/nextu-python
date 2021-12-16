from services.storage import *
from services.cryptocurrency import get_price
from infraestructure.utils import *

def show_general_balance(user_id): 
    all_prices = 0
    print('*****                      INFORME BALANCE GLOBAL                        *****')
    file=open(f'{folder}/user{user_id.id}/balance.txt','r')
    txt = file.read()
    file.close()
    lines = txt.splitlines()
    terms = txt.split("|")
    print(f'MONEDA\t\t CANTIDAD\t\t BALANCE EN USD')
    for line in lines:
        termino = line.split("|")
        total_price = float(get_price(termino[0])) * float(termino[1])
        print(f'{termino[0]}\t\t {termino[1]}\t\t {format_price(total_price)}\t\t')
        all_prices += float(get_price(termino[0])) * float(termino[1])
    print(f'Balance total USD de la cuenta: {format_price(all_prices)}')
