from src.Book import Book
from src.User import User


class Library:
    def __init__(self):
        self.__books : list = []
        self.__users : list = []
        self.__checked_out_books : list = []
        self.__checked_in_books : list = []

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
    def add_book(self, isbn : str, title : str, author : str) -> None:
        self.__books.append([isbn, title, author, True, 0])

    # 1.2 List All Books
    def list_all_books(self) -> None :
        pass

    # 2.1 Check out book
    def check_out_book(self, isbn : str , dni : int , due_date : str) -> str :
        pass

    # 2.2 Check in book
    def check_in_book(self, isbn : str, dni : int , returned_date : str) -> str :
        pass

    # Utils
    def add_user(self, dni, name) -> None :
        pass
