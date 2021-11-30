from services.cryptocurrency import get_cryptonamesandprices, get_price, is_supported_currency
from services.storage import register_transaction

def transfer(logged_user):
    is_currency_valid = False
    while not is_currency_valid:
        currency = input("Ingrese el simbolo de la criptomoneda a transferir: ").lower()
        is_currency_valid = is_supported_currency(currency) 
    is_mount_valid = False
    while not is_mount_valid:
         mount = input("Ingrese la cantidad de la moneda: ").replace(",",".",1)
         is_mount_valid = isa_float(mount)
    is_id_valid = False
    while not is_id_valid:
        id = input("Ingrese el ID correspondiente al destinatario: ")
        is_id_valid = validate_id(id,logged_user.get_id())

      
def isa_float(mount):
    try:
        float(mount)
        return True
    except ValueError:
        print("El dato ingresado no es un numero.")
        return False

def validate_id(id, logged_user):
    try:
        int(id)
        if id != logged_user.get_id():
            return True
        else:
            print(f'El id a transferir no puede ser el mismo al suyo.')
            return False
    except ValueError:
        print("El dato ingresado no es un numero valido.")
        return False

