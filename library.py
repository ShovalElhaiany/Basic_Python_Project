from factory import *
from datetime import *


class Library:
    def __init__(self):
        self.__customers = []
        self.__books = []
        self.__loans = []
        self.__loaned_books = []

    def add_customer(self, customer):
        self.__customers.append(customer)

    def add_book(self, book):
        self.__books.append(book)

    def add_loan(self, loan):
        self.__loans.append(loan)

    def get_book_by_id(self, id):
        for book in self.__books:
            if book.id == id:
                return book

    def loan_book(self, book, customer_id):
        # get the return day
        def get_max_loan_time_per_type():
            if book.book_type == BookType.TEN_DAYS:
                return 10
            elif book.book_type == BookType.FIVE_DAYS:
                return 5
            elif book.book_type == BookType.TWO_DAYS:
                return 2
            else:
                raise NotSuchBookType

        # add book to book list and write the loan
        max_loan_date = datetime.now().date() + timedelta(days=get_max_loan_time_per_type())
        if book in self.__loaned_books:
            raise Exception()
        if customer_id not in (customer.id for customer in self.__customers):
            raise Exception()
        self.__loaned_books.append(book)
        self.__loans.append(Loan(customer_id, book.id, datetime.now().date(), max_loan_date))

    def return_book(self, book_id):
        for loan in self.__loans:
            if loan.book_id == book_id:
                self.__loaned_books.remove(self.get_book_by_id(book_id))
                self.__loans.remove(loan)
                return True

    def display_books(self):
        for book in self.__books:
            if book not in self.__loaned_books:
                print(f"{book.id} - {book.name} By \"{book.author}\" ({book.year_published})\n")

    def display_customers(self):
        for customer in self.__customers:
            print(
                f"Customer ID: {customer.id} | Name: {customer.name}"
                f" | City: {customer.city} | Age: {customer.age}\n")

    def display_loans(self):
        for loan in self.__loans:
            print(
                f"Book ID: {loan.book_id} | Customer ID: {loan.cust_id}"
                f" | Loan Date: {loan.loan_date} | Return Date: {loan.return_date}\n")

    def display_late_loans(self):
        for loan in self.__loans:
            return_date = str(loan.loan_date)
            if datetime.strptime(return_date.strip(), "%Y-%m-%d") < datetime.now():
                print(
                    f"Book ID: {loan.book_id} | Customer ID: {loan.cust_id}"
                    f" | Loan Date: {loan.loan_date} | Return Date: {loan.return_date}\n")

    def find_book_by_name(self, name):
        for book in self.__books:
            if book.name == name:
                return book

    def find_customer_by_name(self, name):
        for customer in self.__customers:
            if customer.name == name:
                return customer

    def remove_book(self, id):
        for book in self.__books:
            if book.id == id:
                self.__books.remove(book)
                return True

    def remove_customer(self, cust_id):
        for customer in self.__customers:
            if customer.id == cust_id:
                self.__customers.remove(customer)
                return True
