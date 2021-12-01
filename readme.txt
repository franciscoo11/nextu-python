formato transacciones:

fecha codigo usuario tipo de operacion moneda cantidad monto 




pipe "|" 


fecha | tipo de operacion | moneda | cantidad | monto----> MONTO USD ACTUALIZADO
formato balance:

monto | cantidad

ADICIONALES:

MANEJO DE ARCHIVOS

DEFINIR FUNCION QUE DADO UN NOMBRE DE ARCHIVO LO CREA SI NO EXISTE, DE LO CONTRARIO LO ABRE

DEFINIR OTRA FUNCION QUE RECIBE EL NOMBRE DEL ARCHIVO Y STRING, PONE EL STRING QUE RECIBE DE PARAMETRO AL FINAL Y LO CIERRA.

PENSAR COMO SERIA LA FUNCION DE PARTIAL CADA LINEA DE TRANSACCION DE BALANCE.

def mostrarBalance():    
    print('*****                        DESPLEGAR BALANCE                               *****')
    archivo=open('balance.txt','r')
    texto = archivo.read()
    archivo.close()
    lineas = texto.splitlines()
    terminos = texto.split("|")
    print("MONEDA\t\t\t" + "CANTIDAD\t")
    for linea in lineas:
        termino = linea.split("|")
        print(termino[0] + "\t" + termino[1] + "\t\t")




# Busco currency balance por simnbolo
    # Actualizo el monto total de la moneda (cryptobalance.amount - amount)
    # Llamamos a register_balance(user,cryptobalance) 

def has_enough_balance(user_id,symbol,amount_trans):
    if get_currencye_amount(user_id,symbol) == None and get_currencye_amount(user_id, symbol).amount < amount_trans:
        return False
    return True

def currencie_in_balance(user_id,symbol):
    open_file = open(f'{folder}/user{user_id}/balance.txt', 'r')
    for line in open_file:
        if symbol in line:
            return True

    return False