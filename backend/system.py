from dataclasses import dataclass , field
from typing import Optional
from account import admin, customer
from book import Book, Series

@dataclass
class System:
    admin: Optional[list] = field(default_factory=list)
    customer: Optional[list] = field(default_factory=list)

    def add_admin(self, admin):
        self.admin.append(admin)

    def add_customer(self, customer):
        self.customer.append(customer)
    
    def add_book(self, book):
        self.book.append(book)

@dataclass
class Seriessystem:
    series: Optional[list] = field(default_factory=list)

    def add_series(self, series):
        self.series.append(series)

server = System(admin=[], customer=[])
admin1 = admin(id="admin", password="admin", name="admin", email="admin", phone="admin", permission="admin" )
admin2 = admin(id="admin2", password="admin2", name="admin2", email="admin2", phone="admin2", permission="admin2")

book1 = Book(book_name="book1", book_id=1, author="author1", detail_in_book="detail1", type="type1", tag="tag1", price=100, img="img1", releae_date="releae_date1", number_of_product=1)

server.add_admin(admin1)
server.add_admin(admin2)
print(server.admin[1])

server.add_book(book1)
print(server.book[0])
