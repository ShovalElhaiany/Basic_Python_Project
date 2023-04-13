from book import *
from customer import *
from exception import *


# program opening message
def welcome():
    print()
    print("Hello user and welcome to the best library in the world :)")
    print()
    print("This is the main menu, to perform an operation, please enter the appropriate number")
    print()


# the user main menu
def main_menu_for_user():
    print("""
    •	1) Add a new customer
    •	2) Add a new book
    •	3) Loan a book
    •	4) Return a book
    •	5) Display all books
    •	6) Display all customers
    •	7) Display all loans
    •	8) Display late loans
    •	9) Find book by name
    •	10) Find customer by name
    •	11) Remove book
    •	12) Remove customer

    •	13)Finish the program""")


def get_int(question):
    value = input(question)
    try:
        value = int(value)
        return value
    except ValueError:
        raise NotInteger


def get_book_type(question):
    value = get_int(question)
    if value not in [member.value for member in BookType]:
        raise NotSuchBookType
    return value


def get_requested_action_by_the_user():
    the_requested_action = get_int("\nEnter requested action: ")
    options = range(1, 14)
    if the_requested_action not in options:
        raise InvalidOption()
    return the_requested_action


def get_user_customer_selection():
    id = get_int("Enter ID: ")
    name = input("Enter Name: ")
    city = input("Enter City: ")
    age = get_int("Enter Age: ")
    new_customer = Customer(id, name, city, age)
    return new_customer


def get_user_book_selection():
    id = get_int("Enter ID: ")
    name = input("Enter Name: ")
    author = input("Enter Author: ")
    year_published = get_int("Enter Year_Published: ")
    type = int(input("Enter Type: "))
    new_book = Book(id, name, author, year_published, type)
    return new_book


def get_user_name_book_selection():
    name_book = input("\nEnter Name of Book: ")
    return name_book


def get_user_id_book_selection():
    id_book = get_int("\nEnter ID Book: ")
    return id_book


def get_user_customer_name_selection():
    customer_name = input("\nEnter Name of Customer: ")
    return customer_name


def get_user_customer_di_selection():
    customer_id = get_int("\nEnter ID of Customer: ")
    return customer_id
