Employee File Management System
Problem Statement
---------------------
Develop a Python application to manage employee details using file handling.
The program should:
Store employee details in a file.
Read employee details from the file.
Display all employees.
Find employees earning more than ₹50,000.
Find the highest-paid employee.
Count employees by role.
Use Classes, Functions, File Handling, Dictionaries, and Exception Handling.
Approach / Logic Used
------------------------
Step 1: Create Employee Class
Employee class contains:
Employee ID
Name
Role
Salary
and a method:
display_details()
Step 2: Store Records
Employee details are written into:
employees.txt
using file handling.
Step 3: Read Records
The file is read line by line and converted into Employee objects.
Step 4: Find Highest Salary
Use:
max()
to identify the highest-paid employee.
Step 5: Count Employees by Role
Use a dictionary to maintain role counts.
Step 6: Exception Handling
Handle missing files using:
FileNotFoundError
How to Run
---------------
Save the program as:
main.py
Open Terminal or Command Prompt.
-----------------------------------
cd question2
Run:
python main.py
Sample Input
----------------
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000
Sample Output
-----------------
===== Employee Details =====
101 - Rahul - Python Developer - ₹50000
102 - Anjali - Tester - ₹45000
103 - John - Developer - ₹60000
104 - Priya - Tester - ₹48000
===== Employees with Salary > 50000 =====
John - ₹60000
Highest Paid Employee:
John - ₹60000
===== Employee Count by Role =====
Python Developer : 1
Tester : 2
Developer : 1

Python Concepts Used
-------------------------
Object-Oriented Programming
-------------------------------
class Employee:
Class
Object
Constructor
Methods
Constructor
-------------
def __init__(self):
File Handling
---------------
open()
read()
write()
append()
Context Manager
----------------
with open()
Functions
------------
add_employee()
read_employees()
find_highest_salary()
find_employees_by_role()
Lists
------
employees = []
Dictionaries
--------------
role_count = {}
Loops
-----
for
Conditional Statements
-------------------------
if
Exception Handling
---------------------
try:
except FileNotFoundError:
Lambda Function
highest = max(employees, key=lambda emp: emp.salary)
