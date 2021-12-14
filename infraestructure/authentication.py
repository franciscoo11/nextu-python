from services.storage import *
from enumerations.loggin_options import *
from infraestructure.menu import menu
from domain.User import User
import sys


init_menu = "S"
def menu_user_authentication():
    open_menu = True
    request_options = True
    while open_menu:
        print(f"""
        {menu_user_options.REGISTER.value} \t\tREGISTRARSE
        {menu_user_options.START_SESION.value} \t\tINICIAR SESION
        """)
        while request_options:
            options = int(input("Ingrese una opcion: "))
            if options < 1 or options > 2:
                print("La opcion ingresada es invalida")
            else:
                request_options = False
                
        if options == menu_user_options.START_SESION.value:
            logged_sesion = start_sesion()
            print("Bienvenido de nuevo! Nos alegra volverte a ver..")
            menu(logged_sesion,init_menu)
        elif options == menu_user_options.REGISTER.value:
            logged_register = register()
            print("Usuario registrado ")
            menu(logged_register,init_menu)
        else:
            sys.exit()






def register():
    loggin_okey = False
    while not loggin_okey:
        user_password = input("Ingrese su clave (MAYOR A 3 CARACTERES): ").upper()
        last_id = int(last_userid())
        user_id = last_id + 1
        loggin_okey = validate_userid(user_id) and len(user_password) > 3
        if loggin_okey == False:
            return_menu = input("Desea volver a ver el menu de inicio? INGRESE S/N:").upper()
            if return_menu == "S":
                menu_user_authentication()
    logged_user = User(user_id)
    create_a_folder(logged_user.id)
    create_filebalance(logged_user.id)
    create_filehystoric(logged_user.id)
    user_register(user_id,user_password)
    if loggin_okey == True:
        print(f'Registro realizado con exito. Su id es: {user_id} y su password es {user_password}')
    return logged_user
    

def validate_userid(user_id):
    try:
        int(user_id)
        return True
        
    except ValueError:
        print("El dato ingresado no es un numero valido.")
        return False

def start_sesion():
    loggin_okey = False
    while not loggin_okey:
        user_id = input("Ingrese su codigo de usuario: ")
        user_password = input("Ingrese su clave mayor a 3 digitos: ").upper()
        loggin_okey = validate_userid(user_id) and len(user_password) > 3 and check_id_pass(user_id,user_password)  
        if loggin_okey == False:
            return_menu = input("Desea volver a ver el menu de inicio? INGRESE S/N:").upper()
            if return_menu == "S":
                menu_user_authentication()
    logged_user = User(user_id)
    if loggin_okey == True:
        print("Usted ha iniciado sesion con exito! ")

    return logged_user

