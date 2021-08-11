from infraestructure.menu import menu
from domain.user import User
print("\nBuenas, bienvenido/a a tu billetera virtual de escritorio \n")

# Setear usuario
# Por codigo (hardcodeado) o autenticacion
user = User(1)

menu(user)