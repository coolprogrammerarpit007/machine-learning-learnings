# Library Managment System

from abc import ABC,abstractmethod

class Person(ABC):
    """ Abstraction base class representing the Person base class in the library."""

    def __init__(self,name,email):
        self._name = name
        self._email = email

    @abstractmethod
    def get_role(self):
        pass

    def contact_info(self):
        print(f"Name: {self._name} and EmailId: {self._email}")


class Member(Person):
    """ Library Member Inherited from Person """

    def __init__(self, name, email,member_id):
        super().__init__(name, email)
        self._member_id = member_id
        self._borrowed_books = []


    def borrow_book(self,book):
        self._borrowed_books.append(book)
        print(f"{self._name} borrowed book name: {book.title}")


    def return_book(self,book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            print(f"{self._name} returned book name: {book.title}")

        else:
            print("Book not found in the book list!")

    def get_role(self):
        return "Member"
    
    @property
    def get_books(self):
        return self._borrowed_books
    

class Librarian(Person):
    def __init__(self, name, email,staff_id):
        super().__init__(name, email)
        self._staff_id = staff_id

    def add_book(self,library,book):
        library._books.append(book)
        print(f"{book.title} added to the library")

    def get_role(self):
        return "Librarian"
    

class Book:
    """ Book Entity """
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    """ Library Class Entity """

    def __init__(self,name):
        self._name = name
        self._books = []
        self._members = []

    def register_member(self,member):
        self._members.append(member)
        print(f"{member.name} is registered to the library.")

    def show_books(self):
        print("Books in the Library")
        for book in self._books:
            print(f"{book.name} written by {book.author}")



library = Library("Universal Library")
librarian = Librarian("Alice Lor","alice@email.com","L1001")
member = Member("Harry Potter","harry.potter@email.com","M1001")
book = Book("Harry Potter and chamber of secrets","JK Rowling","ZER1487")

library.register_member(member)
librarian.add_book(library,book)
library.show_books()
member.borrow_book(book)
member.contact_info()
print(f"Role: {member.get_role()}")   # Polymorphism
print(f"Role: {librarian.get_role()}")# Polymorphism
member.return_book(book)

