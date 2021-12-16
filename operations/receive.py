from services.cryptocurrency import get_cryptonamesandprices, get_price, is_supported_currency
from services.storage import register_transaction, get_currencye_amount
from operations.transfer import *
from services.transaction import receive

def receive(logged_user):
    is_currency_valid = False
    while not is_currency_valid:
        currency = input("Ingrese el simbolo de la criptomoneda a transferir: ").upper()
        is_currency_valid = is_supported_currency(currency) 
        if is_currency_valid == False:
            print("La moneda ingresada no es valida.")
    is_id_valid = False
    while not is_id_valid:
        id_recive = input("Ingrese el ID del usuario que recibe: ")
        is_id_valid = validate_id(id_recive,logged_user) and check_id_exist(id_recive) and int(id_recive) > 0
        if is_id_valid == False:
            print("El id ingresado no es valido.")
    is_mount_valid = False
    currencie_amount = get_currencye_amount(int(id_recive),currency)
    while not is_mount_valid:
         mount = input("Ingrese la cantidad de la moneda: ").replace(",",".",1)
         is_mount_valid = isa_float(mount) and currencie_amount >= float(mount) and currencie_amount > 0
         if is_mount_valid == False:
             print("El monto ingresado no esta disponible.")
    transaction = Transaction(id_recive,logged_user.id,recept_type,currency,float(mount),float(mount)*get_price(currency),datetime.now())
    new_transaction(transaction)