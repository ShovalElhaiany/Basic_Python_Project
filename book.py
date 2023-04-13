from dataclasses import *
from enum import Enum


class BookType(Enum):
    TEN_DAYS = 1
    FIVE_DAYS = 2
    TWO_DAYS = 3


@dataclass
class Book:
    id: int
    name: str
    author: str
    year_published: int
    book_type: BookType
