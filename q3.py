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

# Question 3: Nested Loops
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

#tests
print('n=0')
question_3(0)

print('n=1')
question_3(1)

print('n=7')
question_3(7)