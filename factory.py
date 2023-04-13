from loan import *
from user import *

# csv files
loans_file = open("CSV Files/Loan.csv")
customers_file = open("CSV Files/Customer.csv")
books_file = open("CSV Files/Books.csv")


# Load customers csv file
def load_customers(file, library):
    file.readline()
    for line in file:
        customer_arr = line.split(',')
        customer = Customer(customer_arr[0], customer_arr[1], customer_arr[2], customer_arr[3])
        library.add_customer(customer)


# Load books csv file
def load_books(file, library):
    file.readline()
    for line in file:
        book_arr = line.split(',')
        book = Book(book_arr[0], book_arr[1], book_arr[2], book_arr[3], int(book_arr[4]))
        library.add_book(book)


# Load loans csv file
def load_loans(file, library):
    file.readline()
    for line in file:
        loans_arr = line.split(',')
        loans = Loan(loans_arr[0], loans_arr[1], loans_arr[2], loans_arr[3])
        library.add_loan(loans)


# Activates a method according to the user's choice
def choose_and_activates_the_right_action(user_selection, library):
    if user_selection == 1:
        # Add some customers
        library.add_customer(get_user_customer_selection())
        print("\ncustomer add successfully :)")
    elif user_selection == 2:
        # Add some books
        library.add_book(get_user_book_selection())
        print("\nbook add successfully :)")
    elif user_selection == 3:
        # Loan a book
        book = library.get_book_by_id(get_user_id_book_selection())
        customer_id = (get_user_customer_di_selection())
        library.loan_book(book, customer_id)
    elif user_selection == 4:
        # Return a book
        book = library.return_book(get_user_id_book_selection())
        if book:
            print("\nbook returned successfully :)")
        else:
            print("\nBook not found :(")
    elif user_selection == 5:
        # Display all books
        print("\nAll Books:")
        library.display_books()
        print()
    elif user_selection == 6:
        # Display all customers
        print("\nAll Customers:")
        library.display_customers()
        print()
    elif user_selection == 7:
        # Display all loans
        print("\nAll Loans:")
        library.display_loans()
        print()
    elif user_selection == 8:
        # Display late loans
        library.display_late_loans()
    elif user_selection == 9:
        # Find a book by name
        print("\nFinding book by name:")
        book = library.find_book_by_name(get_user_name_book_selection())
        if book:
            print(f"{book.id} - {book.name} By \"{book.author}\" ({book.year_published})\n")
        else:
            print("\nBook not found :(")
        print()
    elif user_selection == 10:
        # Find a customer by name
        print("\nFinding customer by name:")
        customer = library.find_customer_by_name(get_user_customer_name_selection())
        if customer:
            print(f"Customer ID: {customer.id} | Name: {customer.name}"
                  f" | City: {customer.city} | Age: {customer.age}\n")
        else:
            print("Customer not found :(")
        print()
    elif user_selection == 11:
        # Remove a book
        book = library.remove_book(get_user_id_book_selection())
        if book:
            print("\nbook removed successfully :)")
        else:
            print("Book not found :(")
    elif user_selection == 12:
        # Remove a customer
        customer = library.remove_customer(get_user_customer_di_selection())
        if customer:
            print("\ncustomer removed successfully :)")
        else:
            print("\ncustomer not found :(")
    elif user_selection == 13:
        close_the_program()

    else:
        raise NoSuchOption


# closing the files and exit
def close_the_program():
    books_file.close()
    customers_file.close()
    loans_file.close()
    print("Bye Bye")
    exit()
