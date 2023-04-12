class Series:
    def __init__(self, series_name, last_update, img, what_obj):
        self.series_name = series_name
        self.last_update = last_update
        self.img = img
        self.what_obj = what_obj

class Book_catalog:
    def __init__(self, catalog_name, detail_series, type, tag, img, releae_date):
        self.catalog_name = catalog_name
        self.detail_series = detail_series
        self.type = type
        self.tag = tag
        self.img = img
        self.releae_date = releae_date
        self.catalog_book_list = []

    def add_book_to_catalog(self, book):
        self.catalog_book_list.append(book)

class Book:
    def __init__(self, book_name, book_id, author, detail_in_book, type, tag, price, img, releae_date, number_of_product):
        self.book_name = book_name
        self.book_id = book_id
        self.author = author
        self.detail_in_book = detail_in_book
        self.type = type
        self.tag = tag
        self.price = price
        self.img = img
        self.releae_date = releae_date
        self.number_of_product = number_of_product

    
