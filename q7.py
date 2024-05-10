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

# Question 7: String Manipulation
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
    
# tests
assert question_7("Able was I, ere I saw Elba!") == True
assert question_7("racecar") == True
assert question_7("jello") == False
assert question_7("") == True
assert question_7("B") == True
assert question_7("hey There") == False
assert question_7("123 ! 321") == True

# success message
print('question_7() tests passed')



