from dataclasses import dataclass , field
from typing import Optional


@dataclass
class Series:
    name: str
    last_update: str
    img: str
    what_obj: str


@dataclass
class Book_catalog:
    catalog_name: str
    detail_series: str
    type: str
    tag: str
    img: str
    releae_date: str
    catalog_book_list: Optional[list] = field(default_factory=list)

    def add_book_to_catalog(self, book):
        self.catalog_book_list.append(book)

@dataclass
class Book:
    book_name: str
    book_id: int
    author: str
    detail_in_book: str
    type: str
    tag: str
    price: int
    img: str
    releae_date: str
    number_of_product: int