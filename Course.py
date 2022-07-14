# Python Course class
# this class creates a course object with a course name and grade
# Developer: Chana Lowy
# Date: 1/9/22

import Student
import Roster
from tkinter import*
from tkinter import messagebox


class Course(object):

    def __init__(self, name, semester):
        self.name = name
        self.semester = semester
        self.grades = " "

    def __str__(self):
        rep = self.name + ":" + "\n"
        rep += "Semester: " + self.semester + "\n"
        rep += "Grade: " + self.grades + "\n"
        return rep

    # Function Name- get_name
    # Purpose- returns the calling object's name
    # Parameters- None
    # Return value- self.name (str)
    def get_name(self):
        return self.name

    # Function Name- get_semester
    # Purpose- returns the calling object's semester
    # Parameters- None
    # Return value- self.semester (str)
    def get_semester(self):
        return self.semester

    # Function Name- get_grade
    # Purpose- returns the calling object's grade
    # Parameters- None
    # Return value- self.grades (str)
    def get_grade(self):
        return self.grades

    # Function Name- add_grade
    # Purpose- adds/changes the grade for the course that calls it
    # Parameters- grade (str)
    # Return value- None
    def add_grade(self, grade):
        self.grades = grade
