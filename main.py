from library import *


def main():
    the_best_library = Library()
    load_customers(customers_file, the_best_library)
    load_books(books_file, the_best_library)
    load_loans(loans_file, the_best_library)
    welcome()
    main_menu_for_user()
    while True:
        try:
            user_choice = get_requested_action_by_the_user()
            choose_and_activates_the_right_action(user_choice, the_best_library)
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    main()
