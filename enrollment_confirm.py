from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import Combobox
from db import get_cursor



class EnrollmentConfirm(Frame):
    
    def __init__(self, master, width, height, change_sc_fun, bg, selectedCourses,rollNum):
        Frame.__init__(self, master, width=width, height=height, bg= bg)
        self.change_sc_fun = change_sc_fun
        self.master = master
        self.width = width
        self.height = height
        self.selectedCourses= selectedCourses
        self.rollNum = rollNum
        self.__init_confirm()
    
    def __init_confirm(self):
        customFontPath = "D:/eduplanner/fonts/Montserrat"
        customFont = font.Font(family=customFontPath, weight='bold', size=26)

        # Top bar
        topBar = Label(self, bg='#AB886D', width=self.width, height=8)
        text = Label(topBar, text="ENROLLMENT CONFIRMATION", font=customFont, background='#AB886D', foreground='#420e0b')
        text.place(x=100, y=44)

        backButtonPath = 'D:/eduplanner/assets/images/backButton1.png'
        self.backButton = PhotoImage(file=backButtonPath)
        self.backButton = self.backButton.subsample(7, 8)
        backButton = Button(topBar, image=self.backButton, height=50, width=50, command=self.__backButton, takefocus=False)
        backButton.place(x=15, y=33)
        topBar.pack()

        # Confirmation frame
        confirmationFrame = Frame(self, bg='white', padx=20, pady=20)
        confirmationFrame.pack()

        # Selected courses display
        Label(confirmationFrame, text="Your Selected Courses:", bg='white', font=('Arial', 12)).grid(row=0, column=0, pady=10, sticky=W)
        self.selectedCoursesList = Listbox(confirmationFrame, font=('Arial', 12), width=50, height=10)
        self.selectedCoursesList.grid(row=1, column=0, pady=5, padx=10)

        # Add random highlighting to courses
        for course in self.selectedCourses:
            self.selectedCoursesList.insert(END, course)
        self.__highlight_courses()

    def __highlight_courses(self):
        for i, course in enumerate(self.selectedCourses):
            cursor = get_cursor()
            cursor.execute(f"SELECT courseId FROM Courses WHERE courseName = '{course}'")
            course_id = cursor.fetchall()[0][0]  # Fetch a single course ID
            preReq = cursor.execute(
                f"SELECT preReqCourseId FROM PreReq WHERE courseId = {course_id}"
            ).fetchall()
        
            completed = True
            for id in preReq:
                grade = cursor.execute(
                    f"SELECT grade FROM CoursesStatus WHERE courseId = {id[0]} and rollNumber = {self.rollNum}"
                ).fetchall()
                if not grade or grade[0][0] == 'F':
                    completed = False
                    break
            
            if completed:
                self.selectedCoursesList.itemconfig(i, {'bg': 'lightgreen'})
                self.__insertion(self.rollNum, course_id, cursor)
            else:
                self.selectedCoursesList.itemconfig(i, {'bg': 'lightcoral'}) 

    def __backButton(self):
        from studentenrollment import StudentEnrollment
        self.change_sc_fun(StudentEnrollment(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3",self.rollNum), self)
    
    def __insertion(self, rollNo, courseId, cursor):
        course_id = int(courseId)
        roll_num = int(rollNo)
        cursor.execute(f"INSERT INTO Enrollment(rollNumber,courseId) VALUES ({roll_num},{course_id})")
        cursor.commit()
        messagebox.showinfo("Enrolled", f"You enrolled in the {courseId} of course ")
