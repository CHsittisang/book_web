from dataclasses import dataclass 

@dataclass
class payment:
    payment_id: int
    payment_status: str
    payment_date: str
    payment_detail: str
    payment_price: int
    discount: int

@dataclass
class PrompPay(payment):
    tel_number: str


@dataclass
class CreditCard(payment):
    card_number: str
    card_name: str
    card_date: str
    card_cvv: int

