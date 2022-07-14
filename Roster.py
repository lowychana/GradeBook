# Python HW Rooster class
# this class creates a student rooster, with a list of Student objects ( which each contain courses and grades)
# Developer: Chana Lowy
# Date: 1/9/22

import Student
import Course
import os.path
import pickle
import random
from tkinter import*
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox


# this constructor loads a binary file (if it exists) into self.students
class Roster(object):

    def __init__(self):
        self.students = []
        file_exists = os.path.exists("Grade_Book.dat")
        if file_exists:
            file = open("Grade_Book.dat", "rb")
            self.students = pickle.load(file)
            file.close()

    def __str__(self):
        rep = ""
        for line in self.students:
            rep += str(line) + "\n"
        return rep

    # Function Name- get_student
    # Purpose- return a student object based on the name passed in (once we already know that it exists)
    # Parameters- student_name (str)
    # Return value- student (Student object)
    def get_student(self, student_name):
        for student in self.students:
            if student.get_name() == student_name:
                return student

    # Function Name- add_student
    # Purpose- adds a student object to the roster with the name passed in, if it doesn't already exist
    # Parameters- student_name (str)
    # Return value- None
    def add_student(self, student_name):  # passes in an name inputted by the user
        stu_exists = self.find_student(student_name)  # checks if the student exists
        if not stu_exists:  # if exists is false
            student_id = self.get_a_num()  # generate a random num
            id_exists = self.find_id(student_id)  # check if the ID exists
            while id_exists:  # while the id exists
                student_id = self.get_a_num()  # generate a random num
                id_exists = self.find_id(student_id)  # check if the ID exists
            else:  # if the id doesn't exist
                student1 = Student.Student(student_name, student_id)  # creates a news student object
                self.students.append(student1)  # adds the student to the roster
                messagebox.showinfo(message=student_name + " has been added to the grade book.")
        else:  # if exists is true
            messagebox.showerror(message=student_name + " is already in the grade book and can't be added")

    # Function Name- add_one_student
    # Purpose- adds a student object to the roster, if it doesn't already exist
    # Parameters- None
    # Return value- None
    def add_one_student(self):
        student_name = simpledialog.askstring(title=None, prompt="What is the student's name?")
        if student_name is not None:  # if ok was pressed on the message box
            stu_exists = self.find_student(student_name)  # checks if the student exists
            if not stu_exists:  # if exists is false
                student_id = self.get_a_num()  # generate a random num
                id_exists = self.find_id(student_id)  # check if the ID exists
                while id_exists:  # while the id exists
                    student_id = self.get_a_num()  # generate a random num
                    id_exists = self.find_id(student_id)  # check if the ID exists
                else:  # if the id doesn't exist
                    student1 = Student.Student(student_name, student_id)  # creates a news student object
                    self.students.append(student1)  # adds the student to the roster
                    messagebox.showinfo(message=student_name + " has been added")
            else:  # if student exists is true
                messagebox.showerror(message=student_name + " is already in the grade book and can't be added")

    # Function Name- get_a_random_num()
    # Purpose-  return a random number
    # Parameters- None
    # Return value- num(str)
    @staticmethod
    def get_a_num():
        num = ""
        length = "0123456789"
        for _ in length:
            next_int = random.randint(0, 9)
            num += str(next_int)
        return num

    # Function Name- add_course_to_student
    # Purpose- adds a course object to a student object if the course doesn't exist and the student does
    # Parameters- None
    # Return value- None
    def add_course_to_student(self):
        student_name = simpledialog.askstring(title=None, prompt="What is the student's name?")
        if student_name is not None:  # if a value was entered into the message box
            course_name = simpledialog.askstring(title=None, prompt="What is the course name?")
            if course_name is not None:  # if a value was entered into the message box
                stu_exists = self.find_student(student_name)  # checks if the student exists
                if stu_exists:  # if the student exists
                    student1 = self.get_student(student_name)  # returns the student object
                    cou_exists = student1.find_course(course_name)  # checks if the student is enrolled in course
                    if not cou_exists:  # if the student is not enrolled in the course (false)
                        semester = simpledialog.askstring(title=None, prompt="Which semester? (Fall/Spring/Summer)")
                        if semester is not None:  # if a value was entered into the message box
                            if semester == "Fall" or semester == "Spring" or semester == "Summer":
                                student1.add_course(course_name, semester)
                                messagebox.showinfo(message=course_name + " has been added to the grade book.")
                            else:
                                messagebox.showerror(message="Invalid semester")
                    else:  # if student is enrolled in the course
                        messagebox.showerror(message=student_name + " is already enrolled in this course")
                else:
                    messagebox.showerror(message="This student is not in the grade book")

    # Function Name- find_student
    # Purpose- returns True if the student exists
    # Parameters- student_name (str)
    # Return value- exists (boolean)
    def find_student(self, student_name):
        exists = False
        for student in self.students:
            if student.get_name() == student_name:  # checks if the student already exists
                exists = True
        return exists

        # Function Name- find_id
        # Purpose- returns True if the ID exists
        # Parameters- studentID (str)
        # Return value- exists (boolean)
    def find_id(self, student_id):
        exists = False
        for student in self.students:
            if student.get_id() == student_id:  # checks if the ID already exists
                exists = True
        return exists

    # Function Name- add_grade_to_student
    # Purpose- adds a grade to a certain student's course, if the student is in the roster and enrolled in the course
    # Parameters- None
    # Return value- None
    def add_grade_to_student(self):
        student_name = simpledialog.askstring(title=None, prompt="What is the student's name?")
        if student_name is not None:  # if a value was entered into the message box
            course_name = simpledialog.askstring(title=None, prompt="What is the course name?")
            if course_name is not None:  # if a value was entered into the message box
                grade_name = simpledialog.askstring(title=None, prompt="What is the grade?(A/A-/B+/B/B-/C+/C/D/F)")
                if grade_name is not None:  # if a value was entered into the message box
                    stu_exists = self.find_student(student_name)  # checks if the student exists
                    if stu_exists:  # if the student exists
                        student1 = self.get_student(student_name)  # returns the student object
                        cou_exists = student1.find_course(course_name)  # checks if student is enrolled in course
                        if cou_exists:  # if the student is enrolled in the course
                            course1 = student1.get_course(course_name)   # returns the course
                            if grade_name == "A" or grade_name == "A-" or grade_name == "B+" or grade_name == "B" or \
                                    grade_name == "B-" or grade_name == "C+" or grade_name == "C" or\
                                    grade_name == "D" or grade_name == "F":
                                messagebox.showinfo(message="Grade added")
                                course1.add_grade(grade_name)  # add the grade to the course
                                student1.calc_gpa()  # update the gpa based on the new grade entered
                            else:
                                messagebox.showerror(message="Invalid grade")
                        else:
                            messagebox.showinfo(message=student_name + " is not enrolled in " + course_name)
                    else:
                        messagebox.showerror(message=student_name + " is not in the grade book")

    # Function Name- view_a_student
    # Purpose- prints a student the user asks for if it exists
    # Parameters- student_name (str)
    # Return value- None
    def view_a_student(self, student_name):
        stu_exists = self.find_student(student_name)
        if stu_exists:  # if the student exists
            student1 = self.get_student(student_name)  # returns the student object
        else:
            messagebox.showerror(message="This student does not exist")
            student1 = ""
        return student1

    # Function Name- add_a_text_file
    # Purpose- reads a text file inputted by the user and creates a new student object for each name listed
    # Parameters- None
    # Return value- None
    def add_a_text_file(self):
        my_file = simpledialog.askstring(title=None, prompt="What is the file name? (make sure its a .txt file")
        if my_file is not None:  # if a value was entered into the message box
            this_file_exists = os.path.exists(my_file)
            if this_file_exists:
                file = open(my_file, "r")
                my_lines = file.readlines()
                for line in my_lines:
                    line = line.replace("\n", "")
                    self.add_student(line)
            else:
                messagebox.showerror(message="This file cannot be found. (Try adding .txt)")

    # Function Name- view_roster
    # Purpose- prints the entire roster
    # Parameters- None
    # Return value- None
    def view_roster(self):
        return self

    # Function Name- create_transcript
    # Purpose- creates a file that contains that student's transcript
    # Parameters- None
    # Return value- None
    def create_transcript(self):
        student_name = simpledialog.askstring(title=None, prompt="What is the student's name?")
        if student_name is not None:  # if a value was entered into the message box
            file = open(student_name + "Transcript.txt", "w")  # create a text file with student_nameReportCard.txt
            message = self.view_a_student(student_name)
            if message != "":
                for line in str(message):
                    file.write(line)  # put all the student's info on it
                file.close()
                messagebox.showinfo(title=None, message="A transcript has been created.")

    # Function Name- create_report_card
    # Purpose- creates a file that contains that student's report card
    # Parameters- None
    # Return value- None
    def create_report_card(self):
        student_name = simpledialog.askstring(title=None, prompt="What is the student's name?")
        if student_name is not None:  # if a value was entered into the message box
            stu_exists = self.find_student(student_name)  # checks if the student exists
            if stu_exists:  # if the student exists
                student1 = self.get_student(student_name)  # returns the student object
                semester = simpledialog.askstring(title=None, prompt="What is the semester? (Fall/Spring/Summer)")
                if semester is not None:  # if a value was entered into the message box
                    if semester == "Fall" or semester == "Spring" or semester == "Summer":
                        gpa = student1.calc_gpa_per_semester(semester)
                        # print the report card info for the correct semester
                        file = open(student_name + semester + "ReportCard.txt", "w")  # create text file
                        message = student1.get_name() + "\n" + "---------"
                        message += "\n" + "Student ID: " + student1.get_id() + "\n"
                        message += "GPA: " + str(gpa) + "\n"
                        courses = student1.get_courses()
                        # print only the courses of the correct semester
                        for course in courses:
                            if course.get_semester() == semester:
                                message += str(course) + "\n"
                        # ask for comments and add that too
                        comments = simpledialog.askstring(title=None, prompt="What comments on this report card?")
                        if comments is not None:  # if ok was entered into the message box
                            message += "Comments: " + "\n" + comments + "\n"
                        for line in str(message):
                            file.write(line)  # put all the student's info on it
                        file.close()
                        messagebox.showinfo("A report card has been created")
                    else:  # if invalid semester
                        messagebox.showerror(message="Invalid semester")
            else:  # if the student doesn't exist
                messagebox.showerror(message=student_name + " is not in the grade book")

    # Function Name- save_changes
    # Purpose- saves changes to the roster to a .dat file
    # Parameters- None
    # Return value- None
    def save_changes(self):
        file = open("Grade_Book.dat", "wb")
        pickle.dump(self.students, file)
        file.close()
        messagebox.showinfo("Your changes have been saved")
