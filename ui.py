from enumerations.menu_options import menu_options
from operations.transfer import transfer
from operations.receive import receive
from operations.balance_general import show_general_balance
from operations.balance_crypto import show_singular_balance
from operations.transaction_history import transaction_history
import sys

def menu(logged_user):
    print("Selecciona la operacion a realizar: ")
    back_to_menu = "S"

    request_options = True
    while back_to_menu == "S":
        print(f"""
        {menu_options.TRANSFER.value} - Transferir dinero
        {menu_options.RECIVE.value} - Recibir dinero
        {menu_options.CRYPTOCURRENCY_BALANCE.value} - Balance por moneda
        {menu_options.GENERAL_BALANCE.value} - Balance global
        {menu_options.HISTORYC_TRANSACTIONS.value} - Historial de transacciones
        {menu_options.EXIT_APP.value} - Salir
        """)
    
        while request_options:
            options = input("Ingrese una opcion: ")
            if options == menu_options.TRANSFER.value:
                transfer(logged_user)
                print("Se ha realizado la transferencia con exito!")
                should_restart_menu(logged_user)
            elif options == menu_options.RECIVE.value:
                receive(logged_user)
                print("Se ha realizado la recepción con exito!")
                should_restart_menu(logged_user)
            elif options == menu_options.CRYPTOCURRENCY_BALANCE.value:
                show_singular_balance(logged_user)
                should_restart_menu(logged_user)
            elif options == menu_options.GENERAL_BALANCE.value:
                show_general_balance(logged_user)
                should_restart_menu(logged_user)
            elif options == menu_options.HISTORYC_TRANSACTIONS.value:
                transaction_history(logged_user)
                should_restart_menu(logged_user)
            elif options == menu_options.EXIT_APP.value:
                sys.exit()
            else:
                print("La opcion ingresada no es valida.")


def should_restart_menu(logged_user):
    back_to_menu = input("¿Desea volver al menú principal?, escriba S/N: ").upper()
    if back_to_menu == "N":
        sys.exit()
    else:
        menu(logged_user)
