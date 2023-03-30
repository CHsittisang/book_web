from dataclasses import dataclass , field
from typing import Optional , List
from .account import admin , Account , customer
from .book import Book, Series , Book_catalog




@dataclass
class System:
    admin: Optional[list] = field(default_factory=list)
    customer: Optional[list] = field(default_factory=list)

    def add_admin(self, admin):
        self.admin.append(admin)

    def add_customer(self, customer):
        self.customer.append(customer)
        

system = System()
@dataclass
class Seriessystem:
    series: Optional[list] = field(default_factory=list)

    def add_series(self, series):
        self.series.append(series)

server = System(admin=[], customer=[])
admin1 = admin(id="admin", password="admin", name="admin", email="admin", phone="admin", permission="admin" )
admin2 = admin(id="admin2", password="admin2", name="admin2", email="admin2", phone="admin2", permission="admin2")


book1 = Book(book_name="book1", book_id=1, author="author1", detail_in_book="detail1", type="type1", tag="tag1", price=100, img="img1", releae_date="releae_date1", number_of_product=1)

book1 = Book(book_name="book1", book_id=1, author="author1", detail_in_book="detail1", type="type1", tag="tag1", price=1000, img="img1", releae_date="date1", number_of_product=1)
book2 = Book(book_name="book2", book_id=2, author="author2", detail_in_book="detail2", type="type2", tag="tag2", price=2000, img="img2", releae_date="date2", number_of_product=2)
catalog1= Book_catalog(catalog_name="catalog1", detail_series="detail1", type="type1", tag="tag1", img="img1", releae_date="date1", catalog_book_list=[])
catalog1.add_book_to_catalog(book1)
catalog1.add_book_to_catalog(book2)
Series1 = Series(name="series1", last_update="date1", img="img1", what_obj=catalog1)

Seriescatalog = Seriessystem(series=[])
Seriescatalog.add_series(Series1)


server.add_admin(admin1)
server.add_admin(admin2)
print(server.admin[0])





