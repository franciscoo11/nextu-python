# FUNCION QUE DESPLIEGA EL BALANCE GENERAL DEL USUARIO.
def show_general_balance():    
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