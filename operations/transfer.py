from services.cryptocurrency import get_cryptonamesandprices
from main import logged_user 
def transfer():
    is_currency_valid = False
    while not is_currency_valid:
        currency = input("Ingrese la moneda que desea transferir: ").lower()
        is_currency_valid = validate_namesexist(currency)
    is_mount_valid = False
    while not is_mount_valid:
         mount = input("Ingrese la cantidad de la moneda: ").replace(",",".",1)
         is_mount_valid = isa_float(mount)
    is_id_valid = False
    while not is_id_valid:
        id = input("Ingrese el ID correspondiente al destinatario: ")
        is_id_valid = validate_id(id,logged_user)
        
        



    

# Validar que::
#       currency no es vacio
#       currency es soportado
      

def isa_float(mount):
    try:
        float(mount)
        return True
    except ValueError:
        print("El dato ingresado no es un numero.")
        return False


def validate_namesexist(msj):
    return msj in get_cryptonamesandprices()

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



