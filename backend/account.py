class Account:
    def __init__(self, id, password, name, email, phone):
        self.id = id
        self.password = password
        self.name = name
        self.email = email  
        self.phone = phone

class Admin(Account):
    def __init__(self, id, password, name, email, phone,permission):
            super().__init__( id, password, name, email, phone)
            self.permission = permission
    
    def add_product(self):
        pass

class Customer(Account):
    def __init__(self, id, password,  name, email, phone, address, status = False):
        super().__init__( id, password,  name, email, phone)
        self.address = address
        self.status = status
    
    def view_accountinfo(self):
        pass
    

    
    
    

