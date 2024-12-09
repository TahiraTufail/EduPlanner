from tkinter import *
from tkinter import font
from tkinter.ttk import Treeview
from db import get_cursor


class ViewTable(Frame):
    def __init__(self, master, width, height, change_sc_fun, bg):
        Frame.__init__(self, master, width=width, height=height, bg= bg)
        self.change_sc_fun = change_sc_fun
        self.master = master
        self.width = width
        self.height = height
        self.__init_table()
    
    def __init_table(self):
        customFontPath= "D:/eduplanner/fonts/Montserrat"
        customFont = font.Font(family= customFontPath, weight= 'bold' , size= 26)
        topBar = Label(self, bg='#AB886D', width= self.width, height=8) 
        text = Label(topBar , text= "COURSE PRE-REQ", font= customFont, background= '#AB886D', foreground='#420e0b')
        text.place(x= 100, y= 44)
        backButtonPath = 'D:/eduplanner/assets/images/backButton1.png'
        self.backButton = PhotoImage(file=backButtonPath)
        self.backButton = self.backButton.subsample(7,8)
        backButton = Button(topBar, image= self.backButton, height=50, width=50, command = self.__teacher_pannel, takefocus= False)
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
        cursor.execute("SELECT c.courseId AS CourseID, c.courseName AS CourseName, prereqCourses.courseName AS PreRequisiteName FROM Courses AS c LEFT JOIN PreReq AS p ON c.courseId = p.courseId LEFT JOIN Courses AS prereqCourses ON p.preReqCourseId = prereqCourses.courseId;")
        result = cursor.fetchall()
        for row in result:
            table.insert('', 'end', values=row)
            
        table.pack(fill= "both")
        
    def __teacher_pannel(self):
        from teacherpannel import TeacherPannel
        self.change_sc_fun(TeacherPannel(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3"), self)
        
            
        