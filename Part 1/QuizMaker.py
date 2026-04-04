# CPSC 236 Final Project
# Group Members: Brady Crago, Rachel Forsythe, Lukas Holsopple
# Team Leader: Rachel Forsythe

## QUIZ MAKER ##

import random
import time
import os
import sys
import re
import csv

MAX_TIME = 600  # 10 minutes in seconds
MAX_ID_ATTEMPTS = 3
VALID_CHOICES = ['A', 'B', 'C']

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_student_id(student_id):
    """
    Validates student ID.
    Format: A followed by exactly 5 digits between 1 and 9.
    Example: A12345
    """
    attempts = 0
    valid_id = False
    
    while attempts < 3:
        student_id = input("Enter your ID (Ex. A12345): ")
    
        if len(student_id) == 6:
            if student_id[0] == "A":
                digits_valid = True
    
                for ch in student_id[1:]:
                    if ch < '1' or ch > '9':
                        digits_valid = False
    
                if digits_valid:
                    print("\nID is valid.")
                    valid_id = True
                    break
    
        print("ID is invalid.")
        attempts += 1

def get_student_info():
    """
    Prompts user for first name, last name, and a valid student ID.
    Allows only 3 failed ID attempts.
    """
    fname = input("Enter First Name: ").strip()
    lname = input("Enter Last Name: ").strip()

    attempts = 0
    while attempts < MAX_ID_ATTEMPTS:
        id = input("Enter Student ID (Format: A12345): ").strip()
        if validate_student_id(id):
            return fname, lname, id
        else:
            attempts += 1
            print("Invalid ID format.")

    print("Too many invalid attempts. Program exiting.")
    sys.exit()

def choose_quiz_length():
    """
    Allows student to choose number of questions: 10 or 20.
    """
    while True:
        choice = input("Choose number of questions (10 or 20): ").strip()
        if choice == '10':
            return 10, 1.0
        elif choice == '20':
            return 20, 0.5
        else:
            print("Invalid choice. Enter 10 or 20.")

def load_testbank(filename="testbank.csv"):
    """
    Reads questions from a CSV test bank file.
    Question in column 1, answers A–C in columns 2–4,
    correct answer in column 5.
    """
    if not os.path.exists(filename):
        print("Test bank file not found.")
        sys.exit()

    questions = []

    with open(filename, newline="") as file:
        reader = csv.reader(file)
        header = next(reader)  # skip header row

        for row in reader:
            questions.append({
                "text": (
                    f"{row[0]}\n"
                    f"A) {row[1]}\n"
                    f"B) {row[2]}\n"
                    f"C) {row[3]}"
                ),
                "correct": row[4].strip().upper()
            })

    return questions

def ask_questions(questions, points_per_question):
    """
    Displays questions one at a time, records student answers,
    enforces the 10-minute time limit, and allows redo of incorrect questions.
    """
    start_time = time.time()
    score = 0
    results = []
    incorrect_questions = []

    # First attempt
    for index, q in enumerate(questions, start=1):
        if time.time() - start_time >= MAX_TIME:
            print("\nTime is up! Quiz terminated.")
            break

        print(f"\nQuestion {index}:")
        print(q["text"])

        while True:
            answer = input("Your answer (A/B/C): ").strip().upper()
            if answer in VALID_CHOICES:
                break
            print("Invalid answer. Please enter A, B, or C.")

        correct = q["correct"]

        if answer == correct:
            score += points_per_question
        else:
            incorrect_questions.append(q)

        results.append({
            "question": q["text"],
            "correct": correct,
            "student": answer
        })

    # Redo incorrect questions
    if incorrect_questions:
        print("\nRedo incorrect questions until all are correct.\n")

    while incorrect_questions:
        q = incorrect_questions.pop(0)

        print("\nRedo Question:")
        print(q["text"])

        while True:
            answer = input("Your answer (A/B/C): ").strip().upper()
            if answer in VALID_CHOICES:
                break
            print("Invalid answer. Please enter A, B, or C.")

        if answer != q["correct"]:
            incorrect_questions.append(q)
        else:
            print("Correct!")

    total_time = time.time() - start_time
    return score, total_time, results

def save_results(id, fname, lname, score, elapsed_time, results):
    """
    Saves quiz results to a text file named:
    StudentID_FirstName_LastName.txt
    """
    filename = f"{id}_{fname}_{lname}.txt"

    with open(filename, "w") as file:
        file.write(f"Student ID: {id}\n")
        file.write(f"Name: {fname} {lname}\n")
        file.write(f"Score: {score}\n")
        file.write(f"Elapsed Time: {elapsed_time:.2f} seconds\n\n")

        for i, r in enumerate(results, start=1):
            file.write(f"Question {i}:\n")
            file.write(r["question"] + "\n")
            file.write(f"Correct Answer: {r['correct']}\n")
            file.write(f"Student Answer: {r['student']}\n\n")

def run_quiz():
    """Runs one complete quiz session."""
    clear_screen()
    print("=== Python Quiz Maker ===\n")

    fname, lname, id = get_student_info()
    num_questions, points_per_question = choose_quiz_length()

    all_questions = load_testbank()
    selected_questions = random.sample(all_questions, num_questions)

    score, elapsed_time, results = ask_questions(
        selected_questions, points_per_question
    )

    save_results(id, fname, lname, score, elapsed_time, results)

    print("\nQuiz Completed!")
    print(f"Final Score: {score}")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")

def main():
    """Main program loop."""
    while True:
        run_quiz()
        choice = input("\nEnter Q to quit or S to start a new quiz: ").strip().upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice == 'S':
            continue
        else:
            print("Invalid choice. Exiting.")
            break

if __name__ == "__main__":
    main()
