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

# Question 2: Working with Dictionaries
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
    
# test
test_prices = {'banana': 0.50, 'kiwi': 1.25, 'apple': 0.40, 'watermelon': 1.78, 'strawberry': 0.89}
question_2(test_prices)
