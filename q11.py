""" 
CUSTOMER ENGINEER CODING ASSESSMENT
https://thoughtfulautomation.notion.site/Customer-Engineer-Coding-Challenge-aac0008b43714dbcad6ee01efcc537b3

Import any libraries you might need to answer the questions below here.

Instructions
# This quiz consists of ten questions designed to test your knowledge on Python programming.
# Please take no more than 2 hours on this quiz.
# Handle as many edge cases for each question that you can think of. Write unit tests as needed (none are required though).
# Feel free to use the internet, ChatGPT, or any other resources to help you answer the questions.
# Please share any resources, or links to chats with an AI that you used to answer the questions.
"""

## Challenge Question: Object-Oriented Programming - Library Management System
# Write a Python program to implement a simple library management system using object-oriented programming principles.
# Your program should include classes for Library, Book, and Member.
# In addition to the instructions below, feel free to add any additional methods or attributes you think are necessary or are needed for your implementation.
# Use the following specifications:

    # Book Class:
    # Attributes: title (str), author (str), isbn (str)
    # Methods: None
    # Other Notes
        # print(Book) should return the title and author of the book as follows: "Book.title by Book.author".

    # Member Class:
    # Attributes: name (str), member_id (int), books_checked_out (a list of books the member has checked out)
    # Methods:
    # check_out_book(self, book): Adds a book to the memberâ€™s books_checked_out list if it's available.
    # return_book(self, book): Removes a book from the books_checked_out list.
    # Other Notes
        # print(Member) should return the member's name, ID, and list of books the member has checked out as follows: "Member.name (ID: Member.member_id) - Member.books_checked_out separated by commas".

    # Library Class:
    # Attributes: name (str), books (a list of all Book objects in the library), members (a list of all Member objects).
    # Methods:
    # add_book(self, book): Adds a new book to the library.
    # add_member(self, member): Adds a new member to the library.
    # check_out_book(self, member_id, isbn): Checks out a book to a member.
    # return_book(self, member_id, isbn): Returns a book from a member.
    # get_member_books(self, member_id): Prints out all books checked out by a member.
    # Other Notes
        # print(Library) should return the library's name and the number of books and members in the library as follows: "Library.name - ### books, ### members".

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_checked_out = []
    
    def __str__(self):
        books_checked_out_str = ", ".join([str(book) for book in self.books_checked_out])
        return f"{self.name} (ID: {self.member_id}) - {books_checked_out_str}"

    def check_out_book(self, book):
        if book.is_checked_out:
            print(f"{book.title} is already checked out.")
        else:
            self.books_checked_out.append(book)
            book.is_checked_out = True
            print(f"{self.name} checked out - {book.title}")
           
    def return_book(self, book):
        if book in self.books_checked_out:
            self.books_checked_out.remove(book)
            book.is_checked_out = False
            print(f"{self.name} returned: {book}")
        else:
            print(f"{self.name} has not previously checked out {book.title}.")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def __str__(self):
        num_books = len(self.books)
        num_members = len(self.members)
        return f"{self.name} - {num_books} books, {num_members} members"

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def fetch_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    def fetch_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None   
        
    def check_out_book(self, member_id, isbn):
        curr_member = self.fetch_member(member_id)
        curr_book = self.fetch_book(isbn)

        # check if member exists
        if curr_member == None: print(f"Member {member_id} doesn't exist.")
        # check if book exists
        elif curr_book == None: print(f"Book {isbn} not found.")
        # checkout book
        else: curr_member.check_out_book(curr_book)
        
    def return_book(self, member_id, isbn):
        curr_member = self.fetch_member(member_id)
        curr_book = self.fetch_book(isbn)
        
        # check if member exists
        if curr_member == None: print(f"Member {member_id} doesn't exist.")
        # check if book exists
        elif curr_book == None: print(f"Book {isbn} not found.")
        # return book
        else: curr_member.return_book(curr_book)

    def get_member_books(self, member_id):
        member = self.fetch_member(member_id)
        
        if member:
            print(f"List of books currently checked out by {member.name}:")
            for book in member.books_checked_out:
                print(book)
        else:
            print(f"Member {member_id} doesn't exist.")
         

def challenge_question():
    # code below tests out basic functionality of Library Management System

    book1 = Book("Book1", "Author1", "000-1234567")
    book2 = Book("Book2", "Author2", "000-9889201")
    book3 = Book("Book3", "Author3", "000-0262038")
    book4 = Book("Book4", "Author4", "000-0137059")
    member1 = Member("Alan", 1)
    member2 = Member("Ada", 2)
    member3 = Member("Grace", 3)
    library = Library("Test Library")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    # Add members to the library
    library.add_member(member1)
    library.add_member(member2)
    library.add_member(member3)

    print('LIBRARY INFO')
    print('------------')
    print(library)
    print()

    print("BOOKS CHECKED OUT")
    print("------------------")
    library.check_out_book(1, "000-1234567")  # Alan checks out Book1
    library.check_out_book(2, "000-9889201")  # Ada checks out Book2
    library.check_out_book(3, "000-0262038")  # Grace checks out Book3
    library.check_out_book(1, "000-1234567")  # Alan fails to checkout Book1
    library.check_out_book(1, "000-0137059")  # Alan checks out Book4
    library.check_out_book(1, "000-0000000")  # Alan cannot checkout a book that doesn't exist
    print()

    print('BOOKED CHECKED OUT BY MEMBERS')
    print('-----------------------------')
    library.get_member_books(1)
    library.get_member_books(2)
    library.get_member_books(3)
    library.get_member_books(4)
    print()
    
    print('RETURNS')
    print('-------')
    library.return_book(1, "000-1234567")  # Alan returns Book1
    library.get_member_books(1)

#invoke library system
challenge_question()