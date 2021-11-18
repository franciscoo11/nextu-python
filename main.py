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




history_file = "transactions.txt"
global logged_user 

print("\n Bienvenido/a a tu billetera virtual de escritorio \n")

# Setear usuario
# Por codigo (hardcodeado) o autenticacion
logged_user = User(1)
menu()

