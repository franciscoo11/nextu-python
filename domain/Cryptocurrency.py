class Cryptocurrency:
    def __init__(self, id, symbol, name, price,quantity):
        self.id = id
        self.symbol = symbol
        self.name = name
        self.price = price
        self.quantity = quantity

    def set_quantity(self,quantity):
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity

