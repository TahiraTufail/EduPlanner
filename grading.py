from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import Combobox
from db import get_cursor


class TeacherGrading(Frame):
    def __init__(self, master, width, height, change_sc_fun, bg):
        Frame.__init__(self, master, width=width, height=height, bg=bg)
        self.change_sc_fun = change_sc_fun
        self.master = master
        self.width = width
        self.height = height
        self.__init__grading()

    def __init__grading(self):
        customFontPath = "D:/eduplanner/fonts/Montserrat"
        customFont = font.Font(family=customFontPath, weight='bold', size=26)

        # Top bar
        topBar = Label(self, bg='#AB886D', width=self.width, height=8)
        text = Label(topBar, text="GRADE COURSE", font=customFont, background='#AB886D', foreground='#420e0b')
        text.place(x=100, y=44)

        backButtonPath = 'D:/eduplanner/assets/images/backButton1.png'
        self.backButton = PhotoImage(file=backButtonPath)
        self.backButton = self.backButton.subsample(7, 8)
        backButton = Button(topBar, image=self.backButton, height=50, width=50, command=self.__backButton, takefocus=False)
        backButton.place(x=15, y=33)
        topBar.pack()

        # Grading frame
        gradingFrame = Frame(self, bg='white', padx=190, pady=149)
        gradingFrame.pack()

        # Student ID field
        Label(gradingFrame, text="Student ID:", bg='white', font=('Arial', 12)).grid(row=0, column=0, pady=5, sticky=W)
        self.studentIDEntry = Entry(gradingFrame, font=('Arial', 12), width=30)
        self.studentIDEntry.grid(row=0, column=1, pady=5, padx=10)

        # Course ID field
        Label(gradingFrame, text="Course ID:", bg='white', font=('Arial', 12)).grid(row=1, column=0, pady=5, sticky=W)
        self.courseIDEntry = Entry(gradingFrame, font=('Arial', 12), width=30)
        self.courseIDEntry.grid(row=1, column=1, pady=5, padx=10)
        
        #marks
        Label(gradingFrame, text="Marks", bg='white', font=('Arial', 12)).grid(row=2, column=0, pady=5, sticky=W)
        self.marksEntry = Entry(gradingFrame, font=('Arial', 12), width=30)
        self.marksEntry.grid(row=2, column=1, pady=5, padx=10)
        
        # Submit button
        submitButton = Button(gradingFrame, text="Submit", font=('Arial', 12), bg='#AB886D', fg='white', command=self.__submit_grade)
        submitButton.grid(row=4, column=1, pady=20)
        
        
        #NEXT button
        nextButton = Button(gradingFrame, text="NEXT", font=('Arial', 12), bg='#AB886D', fg= 'white', )

    def __submit_grade(self):
        student_id = self.studentIDEntry.get()
        course_id = self.courseIDEntry.get()
        marks = self.marksEntry.get()

        if not student_id or not course_id:
            self.__show_message("Please fill all fields and select both a course and a grade.")
        else:
            self.selected_grade= ''
            cursor = get_cursor()
            if int(marks) > 85:
                self.selected_grade = 'A*'
            if int(marks) > 75 and int(marks) < 85:
                self.selected_grade = 'A'
            if int(marks) > 65 and int(marks) < 75:
                self.selected_grade = 'B'
            if int(marks) > 55 and int(marks) < 65:
                self.selected_grade = 'C'
            if int(marks) > 45 and int(marks) < 55:
                self.selected_grade = 'D'
            if int(marks) > 35 and int(marks) < 45:
                self.selected_grade = 'E'
            if int(marks) > 0 and int(marks) < 35:
                self.selected_grade = 'F'    
        
        cursor.execute(f"INSERT INTO CoursesStatus(rollNumber,courseId,grade,marks) values ({student_id},{course_id},'{self.selected_grade}',{marks})")
        print("exectued")
        cursor.commit()
        self.__show_message("Grade submitted successfully.")
        
    def __show_message(self, message):
        messageWindow = Toplevel(self)
        messageWindow.title("Message")
        messageWindow.geometry("400x200")
        Label(messageWindow, text=message, font=('Arial', 12), pady=20).pack()
        Button(messageWindow, text="OK", command=messageWindow.destroy).pack(pady=10)

    def __backButton(self):
        from teacherpannel import TeacherPannel
        self.change_sc_fun(TeacherPannel(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3"), self)
    
    
    