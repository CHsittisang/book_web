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
    
    
@dataclass
class customer(Account):
    address: str

    

