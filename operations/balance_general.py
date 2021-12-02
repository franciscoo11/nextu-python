from services.storage import *
# FUNCION QUE DESPLIEGA EL BALANCE GENERAL DEL USUARIO.
def show_general_balance(user_id):    
    print('*****                        DESPLEGAR BALANCE                               *****')
    file=open(f'{folder}/user{user_id.id}/balance.txt','r')
    txt = file.read()
    file.close()
    lines = txt.splitlines()
    terms = txt.split("|")
    print(f'MONEDA | CANTIDAD')
    for line in lines:
        termino = line.split("|")
        print(f'{termino[0]}  {termino[1]}')
    