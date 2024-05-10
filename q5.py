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

# Question 5: Error Handling
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
    
# tests
assert question_5('10','1') == 10
assert question_5(1,0) == -1
assert question_5(2,1) == 2
assert question_5(-7,1) == -7
assert question_5(80,-2) == -40
assert question_5(80,0.5) == 160
assert round(question_5(10,3),2) == 3.33

# success message
print('question_5() tests passed')

