from datetime import datetime
transactions_file = "transactions.txt"
balance_file = "balance.txt"
storage_folder = ""

def historic_register(moneda,transaccion,logged_user,cantidad,price):
    archivo=open('transactions.txt','a+')
    now = datetime.now()
    valor = float(cantidad)*float(price)
    date = str(now.strftime("%d de %B de %Y"))
    archivo.write(date+"|"+moneda+"|"+transaccion+"|"+ logged_user + "|" + str(cantidad) + "|" + str(valor) + "\n")
    archivo.close()

def mostrarHistorico():    
    print('*****                        DESPLEGAR HISTORICO                               *****')
    archivo=open('historicos.txt','r')
    texto = archivo.read()
    archivo.close()
    lineas = texto.splitlines()
    terminos = texto.split("|")
    print("FECHA\t\t\t" + "MONEDA\t" + "TRANSACCION\t\t" + "USUARIO\t\t" + "CANTIDAD\tMONTO")
    for linea in lineas:
        termino = linea.split("|")
        print(termino[0] + "\t" + termino[1] + "\t" + termino[2]+ "\t\t" + termino[3] + "\t\t" + termino[4]+ "\t\t" + termino[4])

