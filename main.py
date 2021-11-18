from infraestructure import menu
from domain.User import User
import requests #import del requests para utilizar get de las API's
import os #import del OS para limpiar la terminal
from datetime import datetime 

def historic_register(moneda,transaccion,logged_user,cantidad,price):
    archivo=open('transactions.txt','a+')
    now = datetime.now()
    valor = float(cantidad)*float(price)
    date = str(now.strftime("%d de %B de %Y"))
    archivo.write(date+"|"+moneda+"|"+transaccion+"|"+ logged_user + "|" + str(cantidad) + "|" + str(valor) + "\n")
    archivo.close()

def mostrarHistorico():    
    print('******************************************************************************************************')
    print('*****                        M O S T R A R   H I S T O R I C O S                                 *****')
    print('******************************************************************************************************')
    archivo=open('historicos.txt','r')
    texto = archivo.read()
    archivo.close()
    lineas = texto.splitlines()
    terminos = texto.split("|")
    print("FECHA\t\t\t" + "MONEDA\t" + "TRANSACCION\t\t" + "USUARIO\t\t" + "CANTIDAD\tMONTO")
    for linea in lineas:
        termino = linea.split("|")
        print(termino[0] + "\t" + termino[1] + "\t" + termino[2]+ "\t\t" + termino[3] + "\t\t" + termino[4]+ "\t\t" + termino[4])


history_file = "transactions.txt"
global logged_user 

print("\n Bienvenido/a a tu billetera virtual de escritorio \n")

# Setear usuario
# Por codigo (hardcodeado) o autenticacion
logged_user = User(1)
menu()

