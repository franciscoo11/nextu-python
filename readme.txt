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


# PENSAR EN UNA FORMA DE LOGGIN PARA INTERCAMBIAR ENTRE USUARIOS SIN SALIR DEL PROGRAMA E INICIAR SESION CON DIFERENTES ID'S.
