class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.upper()
        self.last_name = last_name.upper()

class Student(Person):
    def __init__(self, first_name, last_name, student_id):
        self.student_id = student_id

student = Student('John', 'Doe', '123456')
print(student.first_name)
