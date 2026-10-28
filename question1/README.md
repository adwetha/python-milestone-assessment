Student Marks Management System
Problem Statement
---------------------
Develop a Python program to manage student marks and generate a summary report.
The program should:
Store Student ID, Student Name, Python Marks, SQL Marks, and AI Marks.
Calculate Total Marks and Average Marks.
Assign Grades based on average marks.
Display PASS or FAIL status.
Find the student with the highest average.
Display students scoring above 75 average marks.
Use Lists, Dictionaries, Functions, Conditions, Loops, and List Comprehensions.
Approach / Logic Used
---------------------------
Step 1: Store Student Information
Each student's details are stored in a dictionary and all student records are stored in a list.
Step 2: Calculate Result
For every student:
Total = Python + SQL + AI Marks
Average = Total / 3
Grade is assigned based on Average
PASS if Average ≥ 40
FAIL if Average < 40
Step 3: Find Highest Average
Use the max() function to identify the student with the highest average.
Step 4: Students Above 75
Use a List Comprehension to extract students whose average exceeds 75.
How to Run
---------------
Save the program as:
main.py
Open Terminal or Command Prompt.
cd question1
Run:
python main.py
Sample Input
----------------
Enter number of students: 3

Student 1
ID: 101
Name: Rahul
Python: 80
SQL: 75
AI: 85

Student 2
ID: 102
Name: Anjali
Python: 60
SQL: 65
AI: 70

Student 3
ID: 103
Name: Priya
Python: 90
SQL: 85
AI: 88
Sample Output
-----------------
  Student Result 

Student ID : 101
Name       : Rahul
Total      : 240
Average    : 80.0
Grade      : A
Result     : PASS

Student ID : 102
Name       : Anjali
Total      : 195
Average    : 65.0
Grade      : B
Result     : PASS

Student ID : 103
Name       : Priya
Total      : 263
Average    : 87.67
Grade      : A
Result     : PASS

Highest Scoring Student: Priya

Students above 75:
Rahul, Priya
Python Concepts Used
Lists
students = []
Dictionaries
student = {
    "id": 101,
    "name": "Rahul"
}
Functions
--------------
calculate_grade()
display_student()
Conditional Statements
-------------------------
if
elif
else
Loops
-------
for
List Comprehension
------------------------
top_students = [s["name"] for s in students if s["average"] > 75]
Lambda Function
------------------
max(students, key=lambda x: x["average"])
