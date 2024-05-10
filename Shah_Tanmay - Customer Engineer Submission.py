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

## Question 1: List Comprehension
    # Write a Python program that uses list comprehension to find all numbers between 1 and 20 that are divisible by 2 or 3.
def question_1():
    numbers = [num for num in range(1, 21) if num%3==0 or num%2==0]
    return numbers

## Question 2: Working with Dictionaries
    # Given a dictionary, `prices = {'apple': 0.40, 'banana': 0.50, 'kiwi': 1.25}`,
    # write a Python program to convert the prices into a list of `(fruit, price)` tuples, 
    # then print the list sorted by fruit name.
def question_2(prices):
    fruit_prices = []

    for fruit, price in prices.items():
        fruit_prices.append((fruit,price))
    
    fruit_prices.sort(key=lambda tuple: tuple[0])
    
    for fruit, price in fruit_prices:    
        print(f"{fruit}: {price}")

## Question 3: Nested Loops
# Write a Python program that prints the following pattern using nested loops.
# For n=5, the pattern should look like this:
#    1
#    22
#    333
#    4444
#    55555
def question_3(n):
    # assumption: n must be a non-negative integer
    if type(n)==int and n>=0:
        for level in range(1, n+1):
            pattern = ""
            for num in range(level):
                pattern += str(level)
            print(pattern)

## Question 4: Functions and Namespaces
# Write a function `multiply_by_factor` that takes a list of numbers and a `factor` with which to multiply each number. 
# The function should modify the original list and not return anything.
def question_4(num_list, factor):

    def multiply_by_factor():
        for i, num in enumerate(num_list):
            num_list[i] = num * factor
    
    multiply_by_factor()

## Question 5: Error Handling
# Write a Python program that includes a function divide_numbers which takes two parameters, numerator and denominator. 
# This function should attempt to divide the numerator by the denominator and return the result. 
# However, if the denominator is zero, the function should return -1.
def question_5(numerator, denominator):
    # input check
    if type(numerator) == str: assert numerator.isnumeric()
    if type(denominator) == str: assert denominator.isnumeric()
    numerator = float(numerator)
    denominator = float(denominator)

    # function definition
    def divide_numbers(numerator, denominator):
        return -1 if denominator==0 else numerator/denominator
    
    return divide_numbers(numerator,denominator)

## Question 6: Prime Numbers
# Write a Python program to find and print all the prime numbers between two input values, start and end. 
# Use a function named `find_primes` to accomplish this. 
# A prime number is a number that has exactly two distinct positive divisors: 1 and itself.
def question_6(start, end):
    # ensure valid input
    assert type(start) == int or type(start) == float
    assert type(end) == int or type(end) == float
    assert start <= end
    
    # covert floats into integers
    import math
    if type(start) == float:
        start = int(math.ceil(start))
    if type(end) == float:
        end = int(math.floor(end))
     
    # function definition
    def find_primes(start, end):
        prime_numbers = []
        for num in range(start, end+1):
            if num >= 2:
                is_prime = True
                limit_to_check = int(num**0.5) + 1
                
                for i in range(2, limit_to_check):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_numbers.append(num)

        return prime_numbers
    
    return find_primes(start,end)

## Question 7: String Manipulation
# Given a string, write a Python program to check if it is a palindrome. 
# A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). 
# Your program should include a function named `is_palindrome` that takes a string as an input and returns `True` if it's a palindrome and `False` otherwise.
def question_7(input_string):

    # ignoring spaces, punctuation, and capitalization
    processed_string = ""
    for char in input_string:
        if char.isalnum():
            processed_string += char.lower()

    # function definition
    def is_palindrome(string):
        return string == string[::-1]
    
    return is_palindrome(processed_string)

## Question 8: File Processing
# Write a Python program that does the following:
# 1. Reads a text file with it's named passed as an argument to the program. The file contains a list of words separated by spaces.
# 2. Counts the occurrence of each word in the file
# 3. Writes the counts to a new text file, with name also passed as an argument, in the format word: count, one word per line. 
# 4. The words should be sorted in descending order.
def question_8(input_file_str, output_file_str):
    # Read the input file 
    word_counts = {}
    try:
        with open(input_file_str, 'r') as f:
            words = f.read().split()
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    except Exception as e:
        print("Error opening file:", e)

    # Sort the word counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

    # Write the counts to the output file
    with open(output_file_str, 'w') as f:
        for word, count in sorted_word_counts:
            f.write(f"{word}: {count}\n")


## Question 9: Data Filtering
# Given a list of dictionaries representing different people, write a Python program to filter out those who are not eligible to vote. 
# The criteria for voting eligibility are being at least 18 years old and holding citizenship. 
# Your program should include a function named filter_voters that takes the list of dictionaries and returns a new list containing only the dictionaries of those who are eligible to vote.
# Below is an example list of dictionaries (Note: your program should work for any list of dictionaries with varying structures):
people = [
    {"name": "Alice", "age": 25, "citizenship": "Yes"},
    {"name": "Bob", "age": 17, "Visa": "Yes", "Expiration": "2025-01-01"},
    {"name": "Charlie", "age": 20, "citizenship": "No"},
    {"name": "Raul", "age": 18, "citizenship": "Unknown", "state": "MI"},
    {"name": "David", "age": 30, "citizenship": "Yes", "Visa": "Yes", "Expiration": "2023-01-01"},
    {"name": "Eve", "age": 42, "state": "CA", "citizenship": "Yes", "felony_conviction": "Yes"},
]
def question_9(persons):
    # empty-check
    if persons == []: return []

    # function definition
    def filter_voters(persons):
        eligible_voters = []
        
        for person in persons:
            # assumption: the keys 'age' and 'citizenship' must be present to determine voting status
            if "age" in person and "citizenship" in person:
                if person["age"] >= 18 and person["citizenship"].lower() == "yes":
                    eligible_voters.append(person)
        
        return eligible_voters
    
    return filter_voters(persons)

# Question 10: Recursive Functions
# Write a Python program that implements a recursive function named calculate_fibonacci to find the nth number in the Fibonacci sequence. 
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. 
# Your function should take the term n as an input and return the nth Fibonacci number.
def question_10(n):
    def calculate_fibonacci(n):
        if n==0: 
            return 0
        elif n==1: 
            return 1
        else:
            return calculate_fibonacci(n-2) + calculate_fibonacci(n-1)
    
    # assumption: input must be a non-negative integer
    if type(n)==int and n>=0:
        return calculate_fibonacci(n)


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
    # check_out_book(self, book): Adds a book to the member’s books_checked_out list if it's available.
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
         
# code below tests out basic functionality of Library Management System
def challenge_question():
    book1 = Book("Clean Code: A Handbook of Agile Software Craftsmanship", "Robert C. Martin", "978-0132350884")
    book2 = Book("Design Patterns: Elements of Reusable Object-Oriented Software", "Erich Gamma", "978-0201633610")
    book3 = Book("Introduction to Algorithms", "Thomas H. Cormen and Charles E. Leiserson", "978-0262033848")
    book4 = Book("The Pragmatic Programmer", "Andrew Hunt & David Thomas", "978-0135957059")
    member1 = Member("Alan", 1)
    member2 = Member("Ada", 2)
    member3 = Member("Grace", 3)
    library = Library("Computer Science Library")

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
    library.check_out_book(1, "978-0132350884")  # Alan checks out Clean Code
    library.check_out_book(2, "978-0201633610")  # Ada checks out Design Patterns
    library.check_out_book(3, "978-0262033848")  # Grace checks out Introduction to Algorithms
    library.check_out_book(1, "978-0262033848")  # Alan fails to checkout Introduction to Algorithms
    library.check_out_book(1, "978-0135957059")  # Alan checks out Pragmatic Programmer
    library.check_out_book(1, "000-0000000000")  # Alan cannot checkout a book that doesn't exist
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
    library.return_book(1, "978-0132350884")  # Alan returns Clean Code
    library.get_member_books(1)