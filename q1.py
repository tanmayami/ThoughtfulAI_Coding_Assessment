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

# Question 1: List Comprehension
# Write a Python program that uses list comprehension to find 
# all numbers between 1 and 20 that are divisible by 2 or 3.
def question_1():
    numbers = [num for num in range(1, 21) if num%3==0 or num%2==0]
    return numbers

# test
result = question_1()
expected = [2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
assert result == expected

# success message
print('question_1() test passed')