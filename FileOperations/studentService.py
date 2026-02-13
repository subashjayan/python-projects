import json

from Models.students import Student

def read_students():
    with open('DataSource/students.json', 'r') as file:
        students = file.read()
        print (students)
        return students
    return []


def write_students(students):
    with open('DataSource/students.json', 'w') as file:
        file.write(students)
    return students

def add_student(new_student):
    students = read_students()
    students.append(new_student)
    write_students(students)
    return new_student

def get_all_students():
    students = read_students()
    return students

if(__name__ == "__main__"):
   students = read_students()
   students_data = json.loads(students)
   
   studentObjs = [Student.from_json(student) for student in students_data['students']]

   for student in studentObjs:
    print(student)

   for student in studentObjs:
       print(student.get_student_info())
       