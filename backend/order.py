from account import Customer
class order(Customer):
    def __init__(self,id, password, status, name, email, phone,address,order_id, total_price, order_status, order_date, order_in_cart, shipment_detal):
        super().__init__(order_id, total_price, order_status, order_date, order_in_cart, shipment_detal)
    order_id: int
    total_price: int
    order_status: str
    order_date: str
    order_in_cart: str
    shipment_detal: str

class order_history(order):
    def __init__(self,order_id, total_price, order_status, order_date, order_in_cart, shipment_detal):
        super().__init__(order_id, total_price, order_status, order_date, order_in_cart, shipment_detal)

    def add_order_to_history(self, order):
        if order.order_status == "complete":
            self.order_history_list.append(order)