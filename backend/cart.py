from book import Book
from typing import Optional 
from pydantic import BaseModel, field

class ShoppingCart: 
    product_cart: Optional[list] = field(default_factory=list)

    def add_to_cart_list(self, item):
        self.product_cart.append(item)
    
    def get_cart_list(self):
        return self.product_cart
    
    def get_cart_list_price(self):
        total = 0
        for i in self.product_cart:
            total += i.price
        return total
    
    def get_cart_list_quantity(self):
        total = 0
        for i in self.product_cart:
            total += i.quantity
        return total
    
class 
    
        




    
