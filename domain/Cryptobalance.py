class Cryptobalance:
    def __init__(self, symbol, amount:float):
        self.symbol = symbol
        self.amount = amount
    
    def receive (self,amount:float):
        self.amount += amount
    def send (self,amount):
        self.amount -= amount