class discount:
    code_list = []
    def __init__(self, discount_code, balance, expire_date):
        self.discount_code = discount_code
        self.balance = balance
        self.expire_date = expire_date
        
    def add_discount(self, discount):
        self.code_list.append(discount)

codediscount1 = discount("9999", 100, "01/01/2024")
discount.add_discount(discount,codediscount1)

print(discount.code_list[0].discount_code)

