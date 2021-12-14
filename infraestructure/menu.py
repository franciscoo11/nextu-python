from enumerations.menu_options import menu_options
from operations.transfer import transfer
from operations.receive import receive
from operations.balance_general import show_general_balance
from operations.balance_crypto import show_singular_balance
from operations.transaction_history import transaction_history
import sys
from services.storage import register_transaction

def menu(logged_user,back_to_menu):

    request_options = True
    while back_to_menu == "S":
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
            back_to_menu = show_menu()
            menu(logged_user,back_to_menu)
        elif options == menu_options.RECIVE.value:
            receive(logged_user)
            back_to_menu = show_menu()
            menu(logged_user,back_to_menu)
        elif options == menu_options.CRYPTOCURRENCY_BALANCE.value:
            show_singular_balance(logged_user)
            back_to_menu = show_menu()
            menu(logged_user,back_to_menu)
        elif options == menu_options.GENERAL_BALANCE.value:
            show_general_balance(logged_user)
            back_to_menu = show_menu()
            menu(logged_user,back_to_menu)
        elif options == menu_options.HISTORYC_TRANSACTIONS.value:
            transaction_history(logged_user)
            back_to_menu = show_menu()
            menu(logged_user,back_to_menu)
        else:
            sys.exit()


def show_menu():
    return input("¿Desea volver al menú principal?, escriba S/N: ").upper()
