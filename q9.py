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

# Question 9: Data Filtering
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
    
    
# test
expected = [{"name": "Alice", "age": 25, "citizenship": "Yes"}, 
            {"name": "David", "age": 30, "citizenship": "Yes", "Visa": "Yes", "Expiration": "2023-01-01"},
            {"name": "Eve", "age": 42, "state": "CA", "citizenship": "Yes", "felony_conviction": "Yes"}
            ]
assert question_9(people) == expected

# success message
print('question_9() test passed')


