from dataclasses import dataclass , field
from typing import Optional 
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
    order_history_list: Optional[list] = field(default_factory=list)

    def add_order_to_history(self, order):
        if order.order_status == "complete":
            self.order_history_list.append(order)