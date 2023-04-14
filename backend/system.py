from account import Admin , Account , Customer
from book import Book, Series , Book_catalog

class System:
    def __init__(self):
        self.admin = []
        self.customer  = []
        self.customerlogin = ""

    def add_admin(self, admin: Admin):
        self.admin.append(admin)

    def add_customer(self, customer: Customer):
        self.customer.append(customer)
    
    def customer_login(self, customer: Customer):
        self.customerlogin = customer
    def customer_logout(self, customer: Customer):
        self.customerlogin.remove(customer)


class Seriessystem:
    def __init__(self):
        self.series = []

    def add_series(self, series):
        self.series.append(series)



# runing
server = System()


nut = Customer("nut", "1234", "nut", "email", "phone", "address")
nut1 = Customer("nut1", "1234", "nut1", "email", "phone", "address")
System.add_customer(server , nut)
System.add_customer(server , nut1)
