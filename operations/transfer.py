from services.cryptocurrency import get_cryptonamesandprices, get_price, is_supported_currency
from services.storage import register_transaction, get_currencye_amount
from services.transaction import *
from domain.Transaction import *
from datetime import *

def transfer(logged_user):
    is_currency_valid = False
    while not is_currency_valid:
        currency = input("Ingrese el simbolo de la criptomoneda a transferir: ").upper()
        is_currency_valid = is_supported_currency(currency) 
        if not is_currency_valid:
            print("La moneda ingresada no es valida.")
    is_mount_valid = False
    currencie_amount = get_currencye_amount(logged_user.id,currency)
    while not is_mount_valid:
         mount = input("Ingrese la cantidad de la moneda: ").replace(",",".",1)
         is_mount_valid = isa_float(mount) and currencie_amount >= float(mount) and currencie_amount > 0
         if is_mount_valid == False:
             print("Usted no posee la cantidad que desea tranferir.")
    is_id_valid = False
    while not is_id_valid:
        id_receive = input("Ingrese el ID correspondiente al destinatario: ")
        is_id_valid = validate_id(id_receive,logged_user) and check_id_exist(id_receive)
        if is_id_valid == False:
            print("El id ingresado no es valido.")
    transaction = Transaction(logged_user.id,id_receive,transfer_type,currency,float(mount),float(mount)*get_price(currency),datetime.now())
    new_transaction(transaction)

def isa_float(mount):
    try:
        float(mount)
        return True
    except ValueError:
        print("El dato ingresado no es un numero.")
        return False

def validate_id(id, logged_user):
    try:
        if int(id) != logged_user.get_id():
            return True
        else:
            print(f'El id a transferir no puede ser el mismo al suyo.')
            return False
    except ValueError:
        print("El dato ingresado no es un numero valido.")
        return False
