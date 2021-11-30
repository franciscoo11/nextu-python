from infraestructure.menu import menu
from domain.User import User




history_file = "transactions.txt"

print("\n Bienvenido/a a tu billetera virtual de escritorio \n")

# Setear usuario
# Por codigo (hardcodeado) o autenticacion
logged_user = User(1)
menu(logged_user)

