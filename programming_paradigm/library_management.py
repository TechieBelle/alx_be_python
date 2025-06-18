from xlwings import books


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
         self.__is_checked_out  = True

    def return_book(self):
        self.__is_checked_out = False

    def is_available(self):
        return not self.__is_checked_out


class Library():
    def __init__(self):
        self.__books = []

    def add_book(self,book):
        self.__books.append(book)

    def list_available_books(self):
        for book in self.__books:
            if book.is_available():
                print(f"{book.title} by {book.author}")

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book titled '{title}' not found.")

    def return_book(self, title):
        for book in self.__books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book titled '{title}' not found.")




