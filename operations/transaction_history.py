from services.storage import *
from services.cryptocurrency import get_price
from infraestructure.utils import *

def transaction_history(user_id):
    all_prices = 0
    print('*****                  HISTORIAL DE TRANSACCIONES                    *****')
    file=open(f'{folder}/user{user_id.id}/hystoric_file','r')
    txt = file.read()
    file.close()
    lines = txt.splitlines()
    terms = txt.split("|")
    print(f'FECHA\t\t\t MONEDA\t\t USUARIO\t\t OPERACION\t CANTIDAD\t BALANCE EN USD')
    for line in lines:
        termino = line.split("|")
        total_price = float(get_price(termino[1])) * float(termino[4])
        print(f'{termino[0]}\t {termino[1]}\t\t {termino[2]}\t\t\t {termino[3]}\t {termino[4]}\t\t {format_price(total_price)}')
