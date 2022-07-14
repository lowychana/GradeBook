# Python Student class
# this class creates a student with the attributes of name, as well as a list courses from the courses class
# Developer: Chana Lowy
# Date: 1/9/22

import Roster
import Course


class Student(object):

    def __init__(self, name, student_id):
        self.name = name
        self.studentID = student_id
        self.courses = []
        self.gpa = "0"

    def __str__(self):
        rep = self.name + "\n" + "---------" + "\n"
        rep += "Student ID: " + self.studentID + "\n"
        rep += "GPA: " + str(self.gpa) + "\n"
        for line in self.courses:
            rep += str(line) + "\n"
        return rep

    # Function Name- get_name
    # Purpose-  return the calling object's name
    # Parameters- None
    # Return value- self.name (str)
    def get_name(self):
        return self.name

    # # Function Name- get_a_random_num()
    # # Purpose-  return a random number
    # # Parameters- None
    # # Return value- num(str)
    # def get_a_num(self):
    #     num = ""
    #     length = "0123456789"
    #     for i in length:
    #         next_int = random.randint(0,9)
    #         num += str(next_int)
    #     return num

        # Function Name- get_id
        # Purpose-  return the calling object's ID
        # Parameters- None
        # Return value- self.studentID (str)
    def get_id(self):
        return self.studentID

    # Function Name- get_courses
    # Purpose-  return the calling object's course list
    # Parameters- None
    # Return value- self.courses (list of Course objects)
    def get_courses(self):
        return self.courses

    # Function Name- get_gpa
    # Purpose-  return the calling object's gpa
    # Parameters- None
    # Return value- self.gpa (str)
    def get_gpa(self):
        return self.gpa

    # Function Name- add_course
    # Purpose- adds a course object to the calling object (a Student)
    # Parameters- course_name (str)
    # Return value- None
    def add_course(self, course_name, semester):  # the course name passed in is the name that was inputted by the user
        course1 = Course.Course(course_name, semester)  # create a news course object
        self.courses.append(course1)  # add the course to the student

    # Function Name- find_course
    # Purpose- returns true if the course exists
    # Parameters- course_name
    # Return value- exists (boolean)
    def find_course(self, course_name):
        exists = False
        for course in self.courses:
            if course.get_name() == course_name:  # checks if the student already exists
                exists = True
        return exists

    # Function Name- get_course
    # Purpose-  return a course object based on the name passed in (once we already know that it exists)
    # Parameters- course_name
    # Return value- course (Course object)
    def get_course(self, course_name):
        for course in self.courses:
            if course.get_name() == course_name:
                return course

    # Function Name- calc_gpa
    # Purpose-  calculates the student's current gpa
    # Parameters- None
    # Return value- gpa (str)
    def calc_gpa(self):
        grades = 0.0
        credits = 0.0
        for course in self.courses:  # for each course object in self.courses
            grade = course.get_grade()
            if grade == "A":
                grades += 4.0*3
                credits += 3
            elif grade == "A-":
                grades += 3.67*3
                credits += 3
            elif grade == "B+":
                grades += 3.33*3
                credits += 3
            elif grade == "B":
                grades += 3.0*3
                credits += 3
            elif grade == "B-":
                grades += 2.67*3
                credits += 3
            elif grade == "C+":
                grades += 2.33*3
                credits += 3
            elif grade == "C":
                grades += 2.0*3
                credits += 3
            elif grade == "D":
                grades += 1.0*3
                credits += 3
            elif grade == "F":
                grades += 0.0*3
                credits += 3
        if credits != 0.0:
            gpa = (grades / credits)
            format_gpa = "{:.2f}".format(gpa)
            self.gpa = format_gpa

    # Function Name- calc_gpa
    # Purpose-  calculates the student's gpa for a given semester
    # Parameters- student1 (student object), semester (str)
    # Return value- gpa (str)
    def calc_gpa_per_semester(self, semester):
        grades = 0.0
        credits = 0.0
        for course in self.courses:  # for each course object in self.courses
            grade = course.get_grade()
            if semester == course.get_semester():
                if grade == "A":
                    grades += 4.0 * 3
                    credits += 3
                elif grade == "A-":
                    grades += 3.67 * 3
                    credits += 3
                elif grade == "B+":
                    grades += 3.33 * 3
                    credits += 3
                elif grade == "B":
                    grades += 3.0 * 3
                    credits += 3
                elif grade == "B-":
                    grades += 2.67 * 3
                    credits += 3
                elif grade == "C+":
                    grades += 2.33 * 3
                    credits += 3
                elif grade == "C":
                    grades += 2.0 * 3
                    credits += 3
                elif grade == "D":
                    grades += 1.0 * 3
                    credits += 3
                elif grade == "F":
                    grades += 0.0 * 3
                    credits += 3
            if credits != 0.0:
                gpa = (grades / credits)
                format_gpa = "{:.2f}".format(gpa)
                return format_gpa
