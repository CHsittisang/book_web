class discount:
    def __init__(self, discount_code, balance, expire_date):
        self.discount_code = discount_code
        self.balance = balance
        self.expire_date = expire_date

    def use_discount(self, payment):
        payment.payment_price -= self.balance
 