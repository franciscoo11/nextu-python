from infraestructure.authentication import menu_user_authentication
from infraestructure.menu import menu
from domain.User import User




history_file = "hystoric_file.txt"
print("\n Bienvenido/a a tu billetera virtual de escritorio \n")

# Setear usuario
# Por codigo (hardcodeado) o autenticacion
logged_user = User(1)
menu_user_authentication(logged_user)

