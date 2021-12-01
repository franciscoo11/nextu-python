from services.cryptocurrency import get_cryptonamesandprices, get_price, is_supported_currency
from services.storage import register_transaction, get_currencye_amount
from services.transaction import send

def transfer(logged_user):
    is_currency_valid = False
    while not is_currency_valid:
        currency = input("Ingrese el simbolo de la criptomoneda a transferir: ").upper()
        is_currency_valid = is_supported_currency(currency) 
    is_mount_valid = False
    currencie_amount = get_currencye_amount(logged_user.id,currency)
    while not is_mount_valid:
         mount = input("Ingrese la cantidad de la moneda: ").replace(",",".",1)
         is_mount_valid = isa_float(mount) and currencie_amount >= float(mount)
    is_id_valid = False
    while not is_id_valid:
        id_recive = input("Ingrese el ID correspondiente al destinatario: ")
        is_id_valid = validate_id(id_recive,logged_user)
    send(logged_user.id,id_recive,float(mount),currency)    

    
      
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

