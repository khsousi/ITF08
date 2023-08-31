"""ITF 08 Final Project
TODO 1 Enter your name and submission date
Name : Khaled Waleed El Sousi
Delivery Date : 31-8-2023
Eng.Mohanad Alkrunz
"""

# NOT COMPLETE YET
# NOT COMPLETE YET
# NOT COMPLETE YET
import random


# TODO 2 Define Course Class and define constructor with (course_id generated ,course name (user_input) and
# course mark
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1000, 9999)
        self.course_name = course_name
        self.course_Mark = course_mark


course = Course(course_name="Arabic", course_mark="99")

class Student:
    # TODO 3 define static variable indicate s total student count   #done
    total = 0

    # TODO 4 define a constructor which includes
    # student_id (unique using random module)
    # student_name (user input)
    # student_age (user_inout)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    def __init__(self, student_name, student_age, student_number):
        self.student_id = random.randint(100, 999)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total += 1

student = Student(student_name="khaled", student_age=22, student_number="11")


# TODO 5 define a method to enroll new course to student courses list
    def student_course(self, course_name):
        self.course_list.append(course_name)

    # method to get_student_details as  dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        # # TODO 6 print student courses with their marks
        # print(self.student_name)
        # for i in self.student_course():
        #     print("Course Name: ", student_course(student_name))


    # method to get student_average as a value
    def get_student_average(self):
        pass
    # TODO 7 return the student average


# in Global Scope
# TODO 8 declare empty students list
students_list = []
while True:

    # TODO 9 handle Exception for selection input
    selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))

    if selection == 1:
        student_number = input("Enter Student Number")
        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")

        # TODO 10 create student object and append it to students list
        student = Student(student_number, student_name, student_age)
        students_list.append(student)

        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number")
        # TODO 11 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
    elif selection == 3:
        student_number = input("Enter Student Number")
        # TODO 12 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
    elif selection == 4:
        student_number = input("Enter Student Number")
        # TODO 13 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")
    elif selection == 5:
        student_number = input("Enter Student Number")
        # TODO 14 ask user to enter course name and course mark then create coures object then append it to target student courses
    elif selection == 6:
        exit()
    else:
        print("Invalid Input")
        # TODO 15 call a function to exit the program   #done
