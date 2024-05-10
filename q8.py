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

# Question 8: File Processing
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

# test
input_file = "q8_input.txt"
output_file = "q8_output.txt"
expected_lines = [
    "dog: 4\n",
    "cat: 3\n",
    "mouse: 2\n",
    "eric: 1\n",
    "zoo: 1\n"
]
question_8(input_file, output_file)

with open(output_file, "r") as f:
    output_lines = f.readlines()

assert output_lines == expected_lines
print('question_8() test passed')
