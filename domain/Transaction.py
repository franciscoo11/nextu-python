from datetime import date


class Transaction:
    def __init__(self, origin_id,destination_id,type:str,symbol, amount:float,total_price:float,date):
        self.origin_id = origin_id
        self.destination_id = destination_id
        self.type = type
        self.amount = amount
        self.symbol = symbol
        self.date= date
        self.total_price = total_price
