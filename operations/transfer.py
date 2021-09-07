from services.cryptocurrency import get_cryptonamesandprices

def transfer():
    is_currency_valid = False
    while not is_currency_valid:
        currency = input("Ingrese la moneda que desea transferir: ").lower()
        is_currency_valid = validate_namesexist(currency)
    is_mount_valid = False
    while not is_mount_valid:
         msj = input("Ingrese la cantidad de la moneda: ")
         if len(msj) == 0:
             print("La cantidad no puede estar vacia.")
         is_mount_valid = isa_float(msj)

        
        



    

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

    

def validate_ext(msj):
    if len(msj) == 0:
        print("El dato no puede estar vacio.")
        return False
    
    return True

def validate_namesexist(msj):
    return msj in get_cryptonamesandprices()