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