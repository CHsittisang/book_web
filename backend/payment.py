class payment:
    def __init__(self, payment_id, payment_balance):
        self.payment_id = payment_id
        self.payment_balance = payment_balance


class PrompPay(payment):
    PrompPay_list = []
    def __init__(self, payment_id, payment_balance , tel_number):
        super().__init__(payment_id, payment_balance)
        self.tel_number = tel_number
        
    def add_prompay(self, prompay):
        self.PrompPay_list.append(prompay)
        
    def subtact_balance(self, price):
        self.payment_balance -= price
        
        
        
class CreditCard(payment):
    CreditCard_list = []
    def __init__(self, payment_id, payment_balance, card_number, card_name, card_date, card_cvv):
        super().__init__(payment_id, payment_balance)
        self.card_number = card_number
        self.card_name = card_name
        self.card_date = card_date
        self.card_cvv = card_cvv
        
    def add_creditcard(self, creditcard):
        self.CreditCard_list.append(creditcard)







prompay1 = PrompPay("1", 10000, "0868115450")
creditcard1 = CreditCard("2", 10000, "424242424242", "nut", "01/01/2025", "123")

prompay1.add_prompay(prompay1)
creditcard1.add_creditcard(creditcard1)



print(PrompPay.PrompPay_list[0].tel_number)
print(CreditCard.CreditCard_list[0].card_number)
        