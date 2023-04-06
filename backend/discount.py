from dataclasses import dataclass 

@dataclass
class discount:
    discount_code: str
    balance: int
    expire_date: str

    def use_discount(self, payment):
        payment.payment_price -= self.balance
 