from enumerations.menu_options import menu_options
from operations.transfer import transfer
from operations.receive import receive
from operations.balance_general import show_general_balance
from operations.balance_crypto import show_singular_balance
import sys

def menu(logged_user):
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
            transfer(logged_user)
        elif options == menu_options.RECIVE.value:
            receive(logged_user)
        elif options == menu_options.CRYPTOCURRENCY_BALANCE.value:
            show_singular_balance(logged_user)
        elif options == menu_options.GENERAL_BALANCE.value:
            show_general_balance(logged_user)
        elif options == menu_options.HISTORYC_TRANSACTIONS.value:
            print("Funcion Historial de transacciones")
        else:
            sys.exit()


            

def back_to_menu():
    comeback_to_menu = input("Desea regresar al menu principal? INGRESE S/N: ").upper()
    return comeback_to_menu
