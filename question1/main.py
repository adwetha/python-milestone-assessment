def calculate_grade(avg):
    if avg >=75:
        return "A"
    elif avg>=60:
        return "B"
    elif svg >=40:
        return "C"
    else:
        return "F"

def display_student(student):
    print("\n Student Result")
    print("Student ID :",student["id"]
          )
    print("Name      :",student["name"]
              )
    print("Total     :",student["total"]
              )
    print("Average   :",round(student["average"],2))
    print("grade     :",student["grade"]
              )
    print("Result    :",student["result"]
              )

students=[]

n=int(input("Enter number of students:"))

for i in range(n):
    print(f"\n Enter details for student{i+1}")
    sid=int(input("Student ID: "))
    name=input("Student Name: ")
    python_marks=int(input("Python marks: "))
    sql_marks=int(input("SQL Marks: "))
    ai_marks=int(input("AI marks: "))
    total=python_marks + sql_marks + ai_marks
    average=total/3
    grade=calculate_grade(average)
    result="PASS" if average>=40 else "FAIL"

    student={
    "id":sid,
    "name":name,
    "python":python_marks,
    "sql":sql_marks,
    "ai":ai_marks,
    "total":total,
    "average":average,
    "grade":grade,
    "result":result

    }

    students.append(student)

for student in students:
    display_student(student)

highest_student=max(students,key=lambda x:x["average"])
print("\n Highest scoring Student:",highest_student["name"])
top_students=[student["name"] for student in students
              if student["average"]> 75]
print("Student above 75:",",".join(top_students))
