from dataclasses import *


@dataclass
class Loan:
    cust_id: int
    book_id: int
    loan_date: str
    return_date: str
