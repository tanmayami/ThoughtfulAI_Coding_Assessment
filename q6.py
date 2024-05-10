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

# tests
assert question_6(-1,0) == []
assert question_6(-9,-1) == []
assert question_6(5,5) == [5]
assert question_6(5,7.99) == [5,7]
assert question_6(2.33,7.99) == [3,5,7]
assert question_6(1,9) == [2,3,5,7]
assert question_6(4,25) == [5,7,11,13,17,19,23]
assert question_6(1,100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# success message
print('question_6() tests passed')