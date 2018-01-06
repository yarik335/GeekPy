"""9Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію)."""
from pprint import pprint


def assign_books_ids(book_list):
    """ give id to every book

    id -- consecutive number
    books -- dict to have access to the book by its id
    """
    books = {}
    for i in range(len(book_list)):
        book_list[i].book_id = i + 1  # id in every instance of class Book
        books[i + 1] = book_list[i]  # id in returning dictionary
    return books


class Library:
    """Main class"""

    def __init__(self, available_books, customers):
        self.available_books = available_books
        self.customers = customers

    def give_book(self, book_id):
        """decrease books quantity in library and return book by its id"""
        if self.available_books[book_id].book_quantity > 0:
            self.available_books[book_id].book_quantity -= 1
            return self.available_books[book_id]

    def status(self):
        """Show how Library looks at the moment (user interface?)"""
        print("###### Books ######")
        for k, v in self.available_books.items():
            print("book_id = {}".format(k))
            v.show_book_info()
            print("-------------------------------------------------")
        print("###### Customers ######")
        for c in self.customers:
            c.show_all_information()
            print("-------------------------------------------------")


class Book:
    """ This class represents a book
     Attributes:
        author (Author): instance of Author class represents the author of the book.
        book_name (String): The name of the book.
        book_quantity (int): Number of the book in library.
        pages_quantity (int): Number of pages in the book.
    """

    def __init__(self, author_first_name, author_last_name, author_age, author_years,
                 book_name, book_quantity, pages_quantity):
        self.author = Author(author_first_name, author_last_name, author_age, author_years)
        self.book_name = book_name
        self.book_quantity = book_quantity
        self.pages_quantity = pages_quantity

    def show_author(self):
        """Show info about author
        Do not send any arguments to author method
        """
        self.author.show_all_information()

    def get_name(self):
        return self.book_name

    def show_book_info(self):
        pprint("author - {}".format(self.__dict__['author'].get_name()))
        pprint("book name - {}".format(self.get_name()))
        pprint("book quantity = {}".format(self.__dict__['book_quantity']))
        pprint("book pages quantity = {}".format(self.__dict__['pages_quantity']))


class Person:
    """Class which represent Person

    Attributes:
        first_name (Str): First name of the person.
        last_name (Str): First name of the person.
        age (int): Number of years the person's life.
        name (Str): Person's full name.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.name = first_name.strip() + ' ' + last_name.strip()

    def get_name(self):
        return self.name

    def show_all_information(self):
        """Print all Person information"""
        pprint("First name- {}".format(self.__dict__['first_name']))
        pprint("Last name - {}".format(self.__dict__['last_name']))
        pprint("Age - {}".format(self.__dict__['age']))
        return self.__dict__


class Author(Person):
    """Class which represent author

        Attributes:
            Person attributes
            years (str): Years of authors life.
    """

    def __init__(self, first_name, last_name, age, years):
        Person.__init__(self, first_name, last_name, age)
        self.years = years

    def show_all_information(self):
        """Print out all author information, extends Persons method"""
        pprint("Author name - {}".format(self.__dict__['name']))
        Person.show_all_information(self)
        pprint("Years of life - {}".format(self.years))


class Customer(Person):
    """Class which represent customer of the library

           Attributes:
               Person attributes
               phone_number (str): Personal phone number.
               books (list): List of dictionaries books that customer borrow
       """

    def __init__(self, first_name, last_name, age, phone_number, books):
        Person.__init__(self, first_name, last_name, age)
        self.phone_number = phone_number
        self.books = books

    def get_book(self, library, book_id):
        self.books.append(library.give_book(book_id))

    def show_books(self):
        """Show what books customer borrows"""
        print("books -", end=" ")
        for i in self.books:
            print("{}".format({"book_id": i.book_id, "book_name": i.get_name()}), end="|")
        print()

    def show_all_information(self):
        """Print out all customer information, extends Persons method"""
        pprint("Customer name - {}".format(self.__dict__['name']))
        Person.show_all_information(self)
        pprint("Phone number - {}".format(self.__dict__['phone_number']))
        self.show_books()


def main():
    customer1 = Customer("yarik", "mokhurenko", 21, "+380930527927", [])
    customer2 = Customer("aaaaaa", "ffffffffff", 76, "+380930527927", [])
    customer3 = Customer("nnnnnnn", "oooooooooooo", 13, "+380930527927", [])

    book1 = Book("aaaaaaaaa", "sssssssssssss", 55, "1888-1955", "brave heart", 4, 555)
    book2 = Book("qqqqqq", "rrrrrrrrrr", 21, "1996-2018", "Lost", 2, 5121)
    book3 = Book("wwwwwww", "tttttttttt", 87, "1958-1997", "Angels and deamons", 6, 654)
    book4 = Book("eeeeee", "yyyyyyyyy", 71, "1888-1955", "Kolobok", 10, 45)
    books = [book1, book2, book3, book4]
    customers = [customer1, customer2, customer3]
    lib = Library(assign_books_ids(books), customers)
    lib.status()
    lib.customers[2].get_book(lib, 2)
    lib.customers[0].get_book(lib, 3)
    lib.customers[1].get_book(lib, 1)
    lib.customers[1].get_book(lib, 3)
    lib.status()
    lib.available_books[1].show_author()


if __name__ == '__main__':
    main()
