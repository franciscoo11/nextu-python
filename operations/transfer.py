def transfer():
    is_currency_valid = False
    while not is_currency_valid:
        currency = input("Ingrese la moneda que desea transferir: ") 
        is_currency_valid = validate_currency(currency)

    mount = float(input("Ingrese la cantidad de la moneda: "))
    
    monto = input("Ingrese la cantidad que desea transferir:")
    while not monto.replace(".","",1).isdigit():
        if not monto.replace(".","",1).isdigit():
            print("Ingrese un monto con carácteres numéricos")
            monto=input("Ingrese la cantidad que desea transferir: ")

# Validar que::
#       currency no es vacio
#       currency es soportado
def validate_currency(currency):
    if len(currency) == 0:
        print("El nombre de la moneda no puede estar vacio.")
        return False
    return True
