from services.cryptocurrency import get_cryptonamesandprices, get_price, is_supported_currency
from services.storage import register_transaction, get_currencye_amount
from operations.transfer import *
from services.transaction import receive
from operations.validation import *

def receive(logged_user):
    id_receive = select_id(logged_user)
    currency = select_currency()
    amount = select_amount(id_receive,currency)
    transaction = Transaction(id_receive,logged_user.id,recept_type,currency,float(amount),float(amount)*get_price(currency),datetime.now())
    new_transaction(transaction)