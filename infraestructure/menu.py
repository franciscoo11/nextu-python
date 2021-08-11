from enumerations.menu_options import menu_options
from operations.transfer import transfer
from datetime import datetime   
day = datetime.now()

def menu(user):
    exit_program = False
    request_options = True
    while not exit_program:
        print(f"""
        {menu_options.TRANSFER.value} \t\tTransferir dinero
        {menu_options.RECIVE.value} \t\tRecibir dinero
        {menu_options.CRYPTOCURRENCY_BALANCE.value} \t\tBalance por moneda
        {menu_options.GENERAL_BALANCE.value} \t\tBalance global
        {menu_options.HISTORYC_TRANSACTIONS.value} \t\tHistorial de transacciones
        {menu_options.EXIT_APP.value} \t\tSalir
        """)
    
        while request_options:
            options = int(input("Ingrese una opcion: "))
            if options < 1 or options > 6:
                print("La opcion ingresada es invalida")
            else:
                request_options = False
                
        if options == menu_options.TRANSFER.value:
            transfer()
        elif options == menu_options.RECIVE.value:
            print("Funcion recive")
        elif options == menu_options.CRYPTOCURRENCY_BALANCE.value:
            print("Funcion Balance por moneda")
        elif options == menu_options.GENERAL_BALANCE.value:
            print("Funcion Balance general")
        elif options == menu_options.HISTORYC_TRANSACTIONS.value:
            print("Funcion Historial de transacciones")
        else:
            print("Funcion Salir")
            break



def continue_inprogram():
    continuar= ""
    while continuar != "S":
        continuar = str(input("Desea continuar (S/N")).upper()
        if continuar == "S":
            menu()
        else:
            exit()


            

                