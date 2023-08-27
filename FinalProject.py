import random

class Student:
    total_students = 0

    def __init__(self, student_number, student_name, student_age):
        self.student_id = random.randint(1, 1000)
        self.student_number = student_number
        self.student_name = student_name
        self.student_age = student_age
        self.courses_list = []

        Student.total_students += 1

    def enroll_course(self, course_name, course_mark):
        self.courses_list.append({"course_name": course_name, "course_mark": course_mark})

    def get_student_details(self):
        return {
            "student_id": self.student_id,
            "student_number": self.student_number,
            "student_name": self.student_name,
            "student_age": self.student_age
        }

    def get_student_courses(self):
        if not self.courses_list:
            print("No courses enrolled.")
        else:
            for course in self.courses_list:
                print(f"Course: {course['course_name']}, Mark: {course['course_mark']}")

    def get_student_average(self):
        if not self.courses_list:
            return 0
        total_mark = sum(course['course_mark'] for course in self.courses_list)
        return total_mark / len(self.courses_list)

students = []

while True:
    try:
        selection = int(input("1. Add New Student\n"
                              "2. Delete Student\n"
                              "3. Display Student\n"
                              "4. Get Student Average\n"
                              "5. Add Course to Student with Mark\n"
                              "6. Exit\n"))

        if selection == 1:
            student_number = input("Enter Student Number: ")
            student_name = input("Enter Student Name: ")
            while True:
                try:
                    student_age = int(input("Enter Student Age: "))
                    break
                except ValueError:
                    print("Invalid Value")
            student = Student(student_number, student_name, student_age)
            students.append(student)
            print("Student Added Successfully")

        elif selection == 2:
            student_number = input("Enter Student Number: ")
            for student in students:
                if student.student_number == student_number:
                    students.remove(student)
                    print("Student Deleted Successfully")
                    break
            else:
                print("Student Not Found")

        elif selection == 3:
            student_number = input("Enter Student Number: ")
            for student in students:
                if student.student_number == student_number:
                    print("Student Details:")
                    print(student.get_student_details())
                    break
            else:
                print("Student Not Found")

        elif selection == 4:
            student_number = input("Enter Student Number: ")
            for student in students:
                if student.student_number == student_number:
                    print(f"Student Average: {student.get_student_average()}")
                    break
            else:
                print("Student Not Found")

        elif selection == 5:
            student_number = input("Enter Student Number: ")
            for student in students:
                if student.student_number == student_number:
                    course_name = input("Enter Course Name: ")
                    while True:
                        try:
                            course_mark = float(input("Enter Course Mark: "))
                            break
                        except ValueError:
                            print("Invalid Value")
                    student.enroll_course(course_name, course_mark)
                    print(f"Course '{course_name}' added to the student successfully")
                    break
            else:
                print("Student Not Found")

        elif selection == 6:
            break

        else:
            print("Invalid Selection")

    except ValueError:
        print("Invalid Input")
