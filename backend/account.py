class Account:
    def __init__(self, id, password, name, email, phone):
        self.id = id
        self.password = password
        self.name = name
        self.email = email  
        self.phone = phone
class Customer(Account):
    def __init__(self, id, password,  name, email, phone, address,status = False):
        super().__init__( id, password,  name, email, phone)
        self.order_history_list = []
        self.address = address
        self.status = status
        
