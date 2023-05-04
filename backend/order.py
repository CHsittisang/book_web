from account import *
class Order(Customer):
    oreder_list = []
    def __init__(self,order_id, total_price, order_status, order_date, order_in_cart, shipment_detal):
        super().__init__(order_id, total_price, order_status, order_date, order_in_cart, shipment_detal)
        self.order_id = order_id
        self.total_price = total_price
        self.order_status = order_status
        self.order_date = order_date
        self.order_in_cart = order_in_cart
        self.shipment_detal = shipment_detal
    
    def add_order(self, order):
        self.oreder_list.append(order)

    
class Order_history(Order):
    def __init__(self,order_id, total_price, order_status, order_date, order_in_cart, shipment_detal):
        super().__init__(order_id, total_price, order_status, order_date, order_in_cart, shipment_detal)

    def add_order_to_history(self, order):
        if order.order_status == "complete":
            self.order_history_list.append(order)


nutorder = Order("1", 10000, "complete", "01/01/2021", "1", "1")
    

