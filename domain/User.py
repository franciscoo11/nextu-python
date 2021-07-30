class User:
    def __init__(self, id):
        self.id = id
        self.cryptocurrencys = []
        
    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def get_msj(self):
        return 'hola'



