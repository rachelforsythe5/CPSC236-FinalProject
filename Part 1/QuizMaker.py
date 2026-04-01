# CPSC 236 Final Project
# Group Members: Brady Crago, Rachel Forsythe, Lukas Holsopple
# Team Leader: Rachel Forsythe

## QUIZ MAKER ##

# Import text bank file

import csv

# Get user input
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
id = input("Enter your ID (Ex. A01234): ")


# Validate ID
if len(id) == 6:
    if id[0] == "A":
        print("\nID is valid.")
else:
    for i in range(3):
        print("ID is invalid.")
        id = input("Enter your ID (#x. A01234): ")


# Randomly pick 10 unique questions
import random

selected_questions = random.sample(range(2, 130), 10)
print(selected_questions)


# Display one question at a time
with open("testbank.csv", newline = "") as file:
    reader = csv.reader(file)
    header = next(reader)
    selected_rows = [row for i, row in enumerate(reader) if i in selected_questions]

    answer_list = []
    correct_answers = []
    num_question = 0
    score = 0
    count = 0
    
    for row in selected_rows:
        num_question += 1
        print("\nQuestion", num_question)
        print(row[0])
        print("Option A:", row[1])
        print("Option B:", row[2])
        print("Option C:", row[3])
        
        answer = input("\nAnswer: ")
        answer = answer.upper()
        
        answer_list.append(answer)
        correct_answers.append(row[4])

        if answer_list[count] == correct_answers[count]:
            score += 1
        else:
            pass
        count += 1

    for i in range(10):
        if not answer_list[i] == correct_answers[i]:
            print(answer_list[i], correct_answers[i])


# Invalid answers
print(answer_list)
print(correct_answers)


# Create a text file


# Exit program prompt
