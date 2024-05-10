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
    
# tests
assert question_10(0) == 0
assert question_10(1) == 1
assert question_10(2) == 1
assert question_10(5) == 5
assert question_10(10) == 55

# success message 
print('question_10() tests passed')
