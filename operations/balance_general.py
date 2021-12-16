from services.storage import *
# FUNCION QUE DESPLIEGA EL BALANCE GENERAL DEL USUARIO.
from services.cryptocurrency import get_price
def show_general_balance(user_id): 
    total_price = 0
    print('*****                      INFORME BALANCE GLOBAL                        *****')
    file=open(f'{folder}/user{user_id.id}/balance.txt','r')
    txt = file.read()
    file.close()
    lines = txt.splitlines()
    terms = txt.split("|")
    print(f'MONEDA\t\t CANTIDAD\t\t BALANCE EN USD')
    for line in lines:
        termino = line.split("|")
        print(f'{termino[0]}\t\t {termino[1]}\t\t {format_price(float(get_price(termino[0]))*float(termino[1]))}\t\t')
        total_price += float(get_price(termino[0])) * float(termino[1])
    print(f'Balance total USD de la cuenta: {format_price(total_price)}')


def format_price(x):
    return "{:.2f}".format(x)