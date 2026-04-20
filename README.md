# CPSC236-FinalProject
This repository contains Python code for three projects: a Quiz Maker, a Memory Puzzle, and Othello.
This project was developed as a final group project for CPSC 236.

## Group Members
- Rachel Forsythe (Team Leader)
- Brady Crago
- Lukas Holsopple

## Part 1 - Quiz Maker
### Features
- Student information input with ID validation
- Choice between 10 or 20 questions
- Randomized question selection from a CSV test bank
- 10-minute time limit for quiz completion
- Automatic retry of incorrectly answered questions
- Input validation for multiple-choice answers
- Quiz results saved to a student-specific text file
- Option to restart or quit after each quiz

## Required Files
Make sure the following files are in the same directory:
- QuizMaker.py – main program file
- testbank.csv – question bank file

#### testbank.csv Format
The CSV file must contain:
1. Question text
2. Answer choice A
3. Answer choice B
4. Answer choice C
5. Correct answer (A, B, or C)
The first row should be a header row.

## How to Run
1. Ensure Python 3 is installed.
2. Place **QuizMaker.py** and **testbank.csv** in the same folder.
3. Open a terminal or command prompt.
4. Run the program:
**python QuizMaker.py**

## Scoring
- 10 questions → 1 point each
- 20 questions → 0.5 points each
- Max score: 10

## Output
Results are saved as:
**StudentID_FirstName_LastName.txt**
The file includes:
- Student ID and name
- Final score
- Time taken
- Each question with:
 - Correct answer
 - Student’s answer

- Item 1
 - Nested Item A
 - Nested Item B

1. Step One
 1. Step One-One
 2. Step One-Two

## Part 2 - Memory Puzzle
### Features
- 

## Part 2 - Othello
### Features
- 
