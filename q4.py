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

# Question 4: Functions and Namespaces
# Write a function `multiply_by_factor` that takes a list of numbers and a `factor` with which to multiply each number. 
# The function should modify the original list and not return anything.
def question_4(num_list, factor):
    # assumption num_list is a list of numbers and no type check is needed
    if type(factor) == str: 
        try:
            factor = float(factor)
        except:
            print('Invalid input')
            return

    def multiply_by_factor(num_list, factor):
        for i, num in enumerate(num_list):
            num_list[i] = num * factor
    
    multiply_by_factor(num_list, factor)

# tests
list_1 = [1, 2, 3, 4, 5]
list_2 = [-1, 2, 4, 0, 0.5]
list_3 = []
list_4 = [1, 2, 3]
list_5 = [10, 12]

question_4(list_1, 2) 
question_4(list_2, 0.5) 
question_4(list_3, 0) 
question_4(list_4, '-2')
question_4(list_5, '0.50') 
question_4(list_5, 'Pi') 

assert list_1 == [2, 4, 6, 8, 10]
assert list_2 == [-0.5, 1, 2, 0, 0.25]
assert list_3 == []
assert list_4 == [-2, -4, -6]
assert list_5 == [5, 6]

# success message
print("question_4() tests passed")