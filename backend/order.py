from dataclasses import dataclass 
from account import customer

@dataclass
class order(customer):
    order_id: int
    total_price: int
    order_status: str
    order_date: str
    order_in_cart: str


@dataclass
class order_history(order):
    order_date: str
    order_detel: str