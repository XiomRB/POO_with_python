from student import Student
from teacher import Teacher
from course import Course
from grade import Grade

student = Student('Luis Perez', '1111-1111','Activo')
student.name = 'Panfilo Perez'
teacher = Teacher(10000,'Matemáticas', 1990)
teacher.name = "Patrick Jean"

teacher.getBasicDetails()
print(teacher.canRetire())

student.getBasicDetails()

course = Course(1, 'Matemáticas', None, 6)
grade = Grade(1, 7, student, course)

grade.passed_course()