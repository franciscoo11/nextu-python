from services.cryptocurrency import get_cryptonamesandprices, get_price, is_supported_currency
from services.storage import register_transaction, get_currencye_amount, check_id_exist
from operations.transfer import *
from services.transaction import receive

def select_currency():
    is_currency_valid = False
    while not is_currency_valid:
        currency = input(f"Ingrese el simbolo de la criptomoneda: ").upper()
        is_currency_valid = is_supported_currency(currency) 
        if is_currency_valid == False:
            print("La moneda ingresada no es valida.")

    return currency

def select_amount(id_recive,currency):
    is_mount_valid = False
    currencie_amount = get_currencye_amount(int(id_recive),currency)
    while not is_mount_valid:
         mount = input("Ingrese la cantidad de la moneda: ").replace(",",".",1)
         is_mount_valid = isa_float(mount) and currencie_amount >= float(mount) and currencie_amount > 0
         if is_mount_valid == False:
             print("El monto ingresado no esta disponible.")

    return mount

def select_id(logged_user):
    is_id_valid = False
    while not is_id_valid:
        id_recive = input(f'Ingrese el ID del usuario: ')
        is_id_valid = validate_id(id_recive,logged_user) and check_id_exist(id_recive) and int(id_recive) > 0
        if is_id_valid == False:
            print("El id ingresado no es valido.")

    return id_recive

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
