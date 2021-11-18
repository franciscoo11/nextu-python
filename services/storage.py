from datetime import datetime
transactions_file = "transactions.txt"
balance_file = "balance.txt"
storage_folder = ""

def historic_register(moneda,transaccion,logged_user,cantidad,price):
    archivo=open('transactions.txt','a+')
    now = datetime.now()
    value = float(cantidad)*float(price)
    date = str(now.strftime("%d de %B de %Y"))
    archivo.write(date+"|"+moneda+"|"+transaccion+"|"+ logged_user + "|" + str(cantidad) + "|" + str(value) + "\n")
    archivo.close()

def mostrarBalance():    
    print('*****                        DESPLEGAR HISTORICO                               *****')
    archivo=open('balance.txt','r')
    texto = archivo.read()
    archivo.close()
    lineas = texto.splitlines()
    terminos = texto.split("|")
    print("MONEDA\t\t\t" + "CANTIDAD\t")
    for linea in lineas:
        termino = linea.split("|")
        print(termino[0] + "\t" + termino[1] + "\t" + termino[2]+ "\t\t")

def balance_register(moneda,logged_user,cantidad):
    archivo=open('balance.txt','a+')
    archivo.write(moneda+ "|" + logged_user + "|" + str(cantidad) + "|" + "\n")
    archivo.close()

