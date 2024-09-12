from src.Book import Book
from src.User import User


class Library:
    def __init__(self) -> None:
        self.__books : list[object] = []
        self.__users : list[object] = []
        self.__checked_out_books : list[object] = []
        self.__checked_in_books : list[object] = []

    # Getters
    def get_books(self) -> list:
        return self.__books

    def get_users(self) -> list:
        return self.__users

    def get_checked_out_books(self) -> list:
        return self.__checked_out_books

    def get_checked_in_books(self) -> list:
        return self.__checked_in_books

    # 1.1 Add Book:
    def add_book(self, isbn : str, title : str, author : str) -> list[object]:
        self.__books.append(Book(isbn, title, author, True, 0))
        return self.__books

    # 1.2 List All Books
    def list_all_books(self) -> list :
        return self.__books

    # 2.1 Check out book
    def check_out_book(self, isbn : str , dni : int , due_date : str) -> str :
        return f"User {dni} checked out book {isbn}"
        

    # 2.2 Check in book
    def check_in_book(self, isbn : str, dni : int , returned_date : str) -> str :
        return f"Book {isbn} checked in by user {dni}"

    # Utils
    def add_user(self, dni : int , name : str) -> None :
        self.__users.append(User(dni, name))
