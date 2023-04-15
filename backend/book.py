class Series:
    def __init__(self, series_name, detail_series,last_update, img, author, book_catalog_obj):
        self.series_name = series_name
        self.detail_series = detail_series
        self.last_update = last_update
        self.img = img
        self.author = author
        self.book_catalog_obj = book_catalog_obj

class Book_catalog:
    def __init__(self, catalog_name, type, tag, img, releae_date):
        self.catalog_name = catalog_name
        self.type = type
        self.tag = tag
        self.img = img
        self.releae_date = releae_date
        self.catalog_book_list = []

class Book:
    def __init__(self, book_name, book_id, detail_in_book, type, price, img,  releae_date, number_of_product):
        self.book_name = book_name
        self.book_id = book_id
        self.detail_in_book = detail_in_book
        self.type = type
        self.price = price
        self.img = img
        self.releae_date = releae_date
        self.number_of_product = number_of_product

    
