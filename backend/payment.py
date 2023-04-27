class payment:
    def __init__(self, payment_id, payment_status, payment_date, payment_detail, payment_price, discount):
        self.payment_id = payment_id
        self.payment_status = payment_status
        self.payment_date = payment_date
        self.payment_detail = payment_detail
        self.payment_price = payment_price
        self.discount = discount



class PrompPay(payment):
    def __init__(self, payment_id, payment_status, payment_date, payment_detail, payment_price, discount, tel_number):
        super().__init__(payment_id, payment_status, payment_date, payment_detail, payment_price, discount)
        self.tel_number = tel_number


class CreditCard(payment):
    def __init__(self, payment_id, payment_status, payment_date, payment_detail, payment_price, discount, card_number, card_name, card_date, card_cvv):
        super().__init__(payment_id, payment_status, payment_date, payment_detail, payment_price, discount)
        self.card_number = card_number
        self.card_name = card_name
        self.card_date = card_date
        self.card_cvv = card_cvv