from pydantic import BaseModel
class Student(BaseModel):
    id: int
    name: str
    age: int
    major: str
    gpa: float
    email: str

    def get_student_info(self):
        print (__name__)
        return {
            "Student ID": self.id,
            "Name": self.name,
            "Age": self.age,
            "Major": self.major,
            "GPA": self.gpa,
            "Email": self.email
        }
    
    @classmethod
    def from_json(cls, json_data):
        return cls(
            id=json_data['id'],
            name=json_data['name'],
            age=json_data['age'],
            major=json_data['major'],
            gpa=json_data['gpa'],
            email=json_data['email'],
        )