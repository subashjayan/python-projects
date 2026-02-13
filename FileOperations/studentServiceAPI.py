import json
from fastapi  import FastAPI, HTTPException
from pydantic  import BaseModel
from typing import List, Optional
from Models.students import Student
from studentService import read_students, write_students, add_student, get_all_students

app = FastAPI()

students_db = []
# Sample students
# students_db = [
#     Student(id=1, name="Alice Johnson", email="alice@example.com", age=20, major="Computer Science", gpa=3.8),
#     Student(id=2, name="Bob Smith", email="bob@example.com", age=21, major="Mathematics", gpa=3.5),
#     Student(id=3, name="Charlie Brown", email="charlie@example.com", age=20, major="Physics", gpa=3.9),
# ]

@app.get("/students", response_model=List[Student])
def get_students():
    students = read_students()
    students_data = json.loads(students)   
    studentObjs = [Student.from_json(student) for student in students_data['students']]
    return studentObjs

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for student in students_db:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students", response_model=Student)
def create_student(student: Student):
    students_db.append(student)
    return student

    

