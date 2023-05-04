from account import *
class order(Customer):
    def __init__(self,id, password, status, name, email, phone,address,order_id, total_price, order_status, order_date, order_in_cart, shipment_detal):
        super().__init__(order_id, total_price, order_status, order_date, order_in_cart, shipment_detal)
        self.order_id = order_id
        self.total_price = total_price
        self.order_status = order_status
        self.order_date = order_date
        self.order_in_cart = order_in_cart
        self.shipment_detal = shipment_detal

class order_history(order):
    def __init__(self,order_id, total_price, order_status, order_date, order_in_cart, shipment_detal):
        super().__init__(order_id, total_price, order_status, order_date, order_in_cart, shipment_detal)

    def add_order_to_history(self, order):
        if order.order_status == "complete":
            self.order_history_list.append(order)


    
