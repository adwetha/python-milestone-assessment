class Employee:
  
  def __init__(self, employee_id, name, role, salary):
      self.employee_id = employee_id
      self.name = name
      self.role = role
      self.salary = salary
  def display_details(self):
      print(f"{self.employee_id} - {self.name} - {self.role} - ₹{self.salary}")


def add_employee(employee):
    with open("employees.txt", "a") as file:
        file.write(
             f"{employee.employee_id},{employee.name},{employee.role},{employee.salary}\n"
     )

def read_employees():
     employees = []

     try:
         with open("employees.txt", "r") as file:
             for line in file:
                data = line.strip().split(",")
                employee = Employee(
                int(data[0]),
                data[1],
                data[2],
                int(data[3])
                )

                employees.append(employee)
     except FileNotFoundError:
         print("Error: employees.txt file does not exist.")
     return employees


def find_highest_salary(employees):
    highest = max(employees, key=lambda emp: emp.salary)
    return highest

def find_high_salary_employees(employees):
     return [emp for emp in employees if emp.salary > 50000]


def find_employees_by_role(employees):
     role_count = {}
     for emp in employees:
        role_count[emp.role] = role_count.get(emp.role, 0) + 1
     return role_count


employees_list = [
     Employee(101, "Rahul", "Python Developer", 50000),
     Employee(102, "Anjali", "Tester", 45000),
     Employee(103, "John", "Developer", 60000),
     Employee(104, "Priya", "Tester", 48000)
]
 
with open("employees.txt", "w") as file:
    pass
for emp in employees_list:
     add_employee(emp)

employees = read_employees()
print("===== Employee Details =====")
for emp in employees:
    emp.display_details()

print("===== Employees with Salary > 50000 =====")
high_salary = find_high_salary_employees(employees)

for emp in high_salary:
    print(f"{emp.name} - ₹{emp.salary}")

highest = find_highest_salary(employees)
print(f"Highest Paid Employee: {highest.name} - ₹{highest.salary}"
)
print("===== Employee Count by Role =====")
role_counts = find_employees_by_role(employees)

for role, count in role_counts.items():
    print(f"{role}: {count}")