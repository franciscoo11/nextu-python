from services.storage import *

def transaction_history(user_id):
    print('*****                        HISTORIAL DE TRANSACCIONES                               *****')
    file=open(f'{folder}/user{user_id.id}/hystoric_file.txt','r')
    txt=file.read()
    print(txt)
    