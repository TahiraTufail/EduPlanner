from tkinter import *
from tkinter import font
from tkinter.ttk import Treeview
from db import get_cursor


class Stdcourseview(Frame):
    def __init__(self, master, width, height, change_sc_fun, bg, rollNUm):
        Frame.__init__(self, master, width=width, height=height, bg= bg)
        self.change_sc_fun = change_sc_fun
        self.master = master
        self.width = width
        self.height = height
        self.rollNum= rollNUm
        self.__init_table()
    
    def __init_table(self):
        customFontPath= "D:/eduplanner/fonts/Montserrat"
        customFont = font.Font(family= customFontPath, weight= 'bold' , size= 26)
        topBar = Label(self, bg='#AB886D', width= self.width, height=8) 
        text = Label(topBar , text= "STUDENT'S PORTAL ", font= customFont, background= '#AB886D', foreground='#420e0b')
        text.place(x= 100, y= 44)
        backButtonPath = 'D:/eduplanner/assets/images/backButton1.png'
        self.backButton = PhotoImage(file=backButtonPath)
        self.backButton = self.backButton.subsample(7,8)
        backButton = Button(topBar, image= self.backButton, height=50, width=50, command = self.__student_pannel, takefocus= False)
        backButton.place(x= 15, y= 33)
        topBar.pack()
        table = Treeview(self, column= ("CourseID", "Course Name", "Course Pre Requisite"), show= "headings",height= 24)
        table.heading("CourseID", text= "CourseID")
        table.heading("Course Name" ,text="Course Name")
        table.heading("Course Pre Requisite", text= "Course Pre Requisite")
        
        table.column("CourseID", width=200, anchor=CENTER)
        table.column("Course Name", width=250, anchor=W)
        table.column("Course Pre Requisite", width=250, anchor=CENTER)
        
        cursor = get_cursor()
        cursor.execute(f"SELECT Enrollment.courseId, Courses.courseName FROM Enrollment INNER JOIN Courses ON Enrollment.courseId = Courses.courseId where Enrollment.rollNumber = {self.rollNum}")
        result = cursor.fetchall()
        for row in result:
            table.insert('', 'end', values=row)

        table.pack(fill= "both")
        
    def __student_pannel(self):
        from studentPannel import StudentPannel
        self.change_sc_fun(StudentPannel(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3",self.rollNum), self)
        
            
        