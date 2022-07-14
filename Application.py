# Python Application
# This is the driver class for the Roster, Student and Course classes.
# It allows the user to add students, courses (with their semesters) and classes as well as view a student or a roster.
# A text file can be loaded to add students. Changes can be saved to a .dat file.
# A transcript can be created for each student and saved in a uniquely named text file
# A GPA is calculated for each student
# A report card with comments and a semester gpa can be created for a given semester
# Each student is assigned a unique student id number
# Developer: Chana Lowy
# Date: 1/9/22

import Student
import Roster
import Course
from tkinter import*
from tkinter import ttk
from tkinter import simpledialog


class Application(Frame):

    def __init__(self, master):

        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.lbl = ttk.Label(self, text="Welcome to the grade book!")
        self.lbl.grid(row=0, column=0)
        self.btn0 = ttk.Button(self, text="Quit", command=root.destroy)
        self.btn0.grid(row=1, column=0)
        self.btn1 = ttk.Button(self, text="Add a student", command=myRoster.add_one_student)
        self.btn1.grid(row=1, column=1)
        self.btn2 = ttk.Button(self, text="Add a course", command=myRoster.add_course_to_student)
        self.btn2.grid(row=1, column=2)
        self.btn3 = ttk.Button(self, text="Add/change a grade", command=myRoster.add_grade_to_student)
        self.btn3.grid(row=2, column=0)
        self.btn4 = ttk.Button(self, text="See entire Roster", command=self.see_roster)
        self.btn4.grid(row=2, column=1)
        self.btn5 = ttk.Button(self, text="View a student ", command=self.see_student)
        self.btn5.grid(row=2, column=2)
        self.btn6 = ttk.Button(self, text="Add students from file", command=myRoster.add_a_text_file)
        self.btn6.grid(row=3, column=0)
        self.btn7 = ttk.Button(self, text="Create a transcript", command=myRoster.create_transcript)
        self.btn7.grid(row=3, column=1)
        self.btn8 = ttk.Button(self, text="Create a report card", command=myRoster.create_report_card)
        self.btn8.grid(row=3, column=2)
        self.btn9 = ttk.Button(self, text="Save Changes", command=myRoster.save_changes)
        self.btn9.grid(row=4, column=0)

    def see_roster(self):
        self.txtDesc = Text(self, width=35, height=15, wrap=WORD)
        self.txtDesc.grid(row=5, column=0, columnspan=3, sticky=W)
        message = myRoster.view_roster()
        # clear out the text box
        self.txtDesc.delete(0.0, END)
        # insert string into text widget
        self.txtDesc.insert(0.0, message)

    def see_student(self):
        student_name = simpledialog.askstring(title=None, prompt="Which student's grades would you like to see?")
        if student_name is not None:  # if a value was entered into the message box
            message = myRoster.view_a_student(student_name)
            if message != "":
                self.txtDesc = Text(self, width=35, height=15, wrap=WORD)
                self.txtDesc.grid(row=5, column=0, columnspan=3, sticky=W)
                # clear out the text box
                self.txtDesc.delete(0.0, END)
                # insert string into text widget
                self.txtDesc.insert(0.0, message)


# main
myRoster = Roster.Roster()
# create root window
root = Tk()
# create title
root.title("Grade Book Program")
# sizing
root.geometry("400x400")
app = Application(root)
root.mainloop()
