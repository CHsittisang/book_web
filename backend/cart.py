class Cart: 
    def __init__(self):
        self.product_cart = []
        

    def add_to_cart_list(self, item):
        print("Adding item to cart")
        self.product_cart.append(item)
    
    def get_cart_list(self):
        return self.product_cart
    
    def get_cart_list_price(self):
        total = 0
        for i in self.product_cart:
            total += int(i.price)
        return total
    
    def get_cart_list_quantity(self):
        total = 0
        for i in self.product_cart:
            total += i.quantity
        return total
    
    def clear_cart_list(self):
        self.product_cart.clear()

    


cart = Cart()

    
    
