from services.transaction import *
from domain.Transaction import *
from operations.validation import *
from datetime import *

def transfer(logged_user):
    id_receive = select_id(logged_user)
    currency = select_currency()
    amount = select_amount(logged_user.id,currency)
    transaction = Transaction(logged_user.id,id_receive,transfer_type,currency,float(amount),float(amount)*get_price(currency),datetime.now())
    new_transaction(transaction)
