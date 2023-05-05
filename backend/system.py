from account import *
from book import Book, Series , Book_catalog
import csv

class System:
    count_account = 0
    def __init__(self):
        self.customer  = []
        self.customerlogin = []

    def add_customer(self, customer: Customer):
        self.customer.append(customer)
    
    def add_customerlogin(self, customer: Customer):
        self.customerlogin.append(customer)
    
    def add_order_to_history(self, order):
            self.order_history_list.append(order)
        
class Seriessystem:
    current_series = 0
    def __init__(self):
        self.series = []
        self.book_catalog_list = []
        self.book_list = []

    def add_series(self, series):
        self.series.append(series)
        
    def read_series_data(self, file_name):
        with open(file_name, mode='r',encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                series_name = row['series_name']
                detail_series = row['detail_series']
                last_update = row['last_update']
                img = row['img']
                author = row['author']
                book_catalog_obj = row['book_catalog_obj']
                self.series.append(Series(series_name, detail_series, last_update, img, author, book_catalog_obj))
                
    def read_book_catalog_data(self, file_name):
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                catalog_name = row['catalog_name']
                type = row['type']
                tag = row['tag']
                img = row['img']
                release_date = row['relea_date']
                book_catalog_obj = Book_catalog(catalog_name, type, tag, img, release_date)
                self.book_catalog_list.append(book_catalog_obj)
                catalog_book_list = row['catalog_book_list'].split(';')
                for book_id in catalog_book_list:
                    for book in self.book_list:
                        if book.book_id == book_id:
                            book_catalog_obj.catalog_book_list.append(book)

    def read_book_data(self, file_name):
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                book_name = row['book_name']
                book_id = row['book_id']
                detail_in_book = row['detail_in_book']
                type = row['type']
                price = row['price']
                img = row['img']
                release_date = row['relea_date']
                number_of_product = row['number_of_product']
                self.book_list.append(Book(book_name, book_id, detail_in_book, type, price, img, release_date, number_of_product))



# runing
server = System()
serverseries = Seriessystem()
serverseries.read_series_data("backend/data/series.csv")
serverseries.read_book_catalog_data("backend/data/book_catalog.csv")
serverseries.read_book_data("backend/data/book.csv")

Guest = Customer("Guest", "1234", "Guest", "email", "phone", "address")
nut = Customer("nut", "1234", "nut", "email", "phone", "address")
nut1 = Customer("nut1", "1234", "nut1", "email", "phone", "address")
# top = Customer("top", "1234", "top", "top@email.com", "0982843051", "in the world")
System.add_customer(server , Guest)
System.add_customer(server , nut)
System.add_customer(server , nut1)
# System.add_customer(server , top)