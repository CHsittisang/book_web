from dataclasses import dataclass

@dataclass
class Account:
    id: str
    password: str
    name: str
    email: str
    phone: str

@dataclass
class admin(Account):
    permission: str

    def add_book(self):
        pass

@dataclass
class customer(Account):
    address: str

    

