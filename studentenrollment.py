from tkinter import *
from tkinter import font
from tkinter.ttk import Combobox
from db import get_cursor
from enrollment_confirm import EnrollmentConfirm



class StudentEnrollment(Frame):
    
    def __init__(self, master, width, height, change_sc_fun, bg, rollNum):
        Frame.__init__(self, master, width=width, height=height, bg= bg)
        self.change_sc_fun = change_sc_fun
        self.master = master
        self.width = width
        self.height = height
        self.rollNum = rollNum
        self.__init__std_enroll()

    def __init__std_enroll(self):
        customFontPath = "D:/eduplanner/fonts/Montserrat"
        customFont = font.Font(family=customFontPath, weight='bold', size=26)

        # Top bar
        topBar = Label(self, bg='#AB886D', width=self.width, height=8)
        text = Label(topBar, text="COURSE SELECTION", font=customFont, background='#AB886D', foreground='#420e0b')
        text.place(x=100, y=44)

        backButtonPath = 'D:/eduplanner/assets/images/backButton1.png'
        self.backButton = PhotoImage(file=backButtonPath)
        self.backButton = self.backButton.subsample(7, 8)
        backButton = Button(topBar, image=self.backButton, height=50, width=50, command=self.__backButton, takefocus=False)
        backButton.place(x=15, y=33)
        topBar.pack()

        # Course selection frame
        selectionFrame = Frame(self, bg='white', padx=20, pady=20)
        selectionFrame.pack()

        # Courses dropdown
        Label(selectionFrame, text="Select Course:", bg='white', font=('Arial', 12)).grid(row=0, column=0, pady=5, sticky=W)
        cursor = get_cursor()
        courses = cursor.execute("SELECT courseName  FROM Courses").fetchall()
        self.courses = [] 
        for course in courses:
            self.courses.append(course[0])
        self.selected_courses = []

        self.courseDropdown = Combobox(selectionFrame, values=self.courses, font=('Arial', 12), state='readonly', width=28)
        self.courseDropdown.grid(row=0, column=1, pady=5, padx=10)
        self.courseDropdown.set("Select a Course")

        addButton = Button(selectionFrame, text="Add", font=('Arial', 12), bg='#AB886D', fg='white', command=self.__add_course)
        addButton.grid(row=0, column=2, padx=10)

        # Selected courses display
        Label(selectionFrame, text="Selected Courses:", bg='white', font=('Arial', 12)).grid(row=1, column=0, pady=10, sticky=W)
        self.selectedCoursesList = Listbox(selectionFrame, font=('Arial', 12), width=50, height=10)
        self.selectedCoursesList.grid(row=2, column=0, columnspan=3, pady=5)
        
        removeButton = Button(selectionFrame, text="Remove", font=('Arial', 12), bg='#AB886D', fg='white', command=self.__remove_course)
        removeButton.grid(row=3, column=1, pady=10)
        
        nextButton = Button(selectionFrame, text="Next", font=('Arial', 12), bg='#AB886D', fg='white', command=self.__next_screen)
        nextButton.grid(row=4, column=1, pady=10)

    def __add_course(self):
        selected_course = self.courseDropdown.get()
        if selected_course != "Select a Course" and selected_course in self.courses:
            self.selected_courses.append(selected_course)
            self.courses.remove(selected_course)
            self.courseDropdown['values'] = self.courses
            self.courseDropdown.set("Select a Course")
            self.selectedCoursesList.insert(END, selected_course)
            
    def __remove_course(self):
        selected_index = self.selectedCoursesList.curselection()
        if selected_index:
            selected_course = self.selectedCoursesList.get(selected_index)
            self.selected_courses.remove(selected_course)
            self.courses.append(selected_course)
            self.courseDropdown['values'] = self.courses
            self.selectedCoursesList.delete(selected_index)

    def __backButton(self):
        from studentPannel import StudentPannel
        self.change_sc_fun(StudentPannel(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3",self.rollNum), self)
        
    def __next_screen(self):
        from enrollment_confirm import EnrollmentConfirm
        if isinstance(self.rollNum, list):
            self.rollNum1 = self.rollNum[0]
            eachRollNum = int(self.rollNum1)
            print(f"rollNum1: {eachRollNum}, Type: {type(eachRollNum)}")

        else:
            self.rollNum1 = int(self.rollNum)
            print(f"rollNum1: {self.rollNum1}, Type: {type(self.rollNum1)}")

        self.change_sc_fun(EnrollmentConfirm(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3", self.selected_courses, self.rollNum),self )
