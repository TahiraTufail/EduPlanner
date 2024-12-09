
from tkinter import *
from tkinter import font
from tkinter.ttk import Treeview

from db import get_cursor

class ViewGrades(Frame):
    def __init__(self, master, width, height, change_sc_fun, bg,rollNum):
         Frame.__init__(self, master, width=width, height=height, bg= bg)
         self.change_sc_fun = change_sc_fun
         self.master = master
         self.width = width
         self.height = height
         self.rollNum = rollNum
         self.__show_grades()
    
    def __show_grades(self):
        customFontPath= "D:/eduplanner/fonts/Montserrat"
        customFont = font.Font(family= customFontPath, weight= 'bold' , size= 26)
        topBar = Label(self, bg='#AB886D', width= self.width, height=8) 
        text = Label(topBar , text= "STUDENT GRADES ", font= customFont, background= '#AB886D', foreground='#420e0b')
        text.place(x= 100, y= 44)
        backButtonPath = 'D:/eduplanner/assets/images/backButton1.png'
        self.backButton = PhotoImage(file=backButtonPath)
        self.backButton = self.backButton.subsample(7,8)
        backButton = Button(topBar, image= self.backButton, height=50, width=50, command = self.__std_pannel, takefocus= False)
        backButton.place(x= 15, y= 33)
        topBar.pack()
        table = Treeview(self, column= ("CourseID", "Course Name", "Roll Number","Grades"), show= "headings",height= 24)
        table.heading("CourseID", text= "CourseID")
        table.heading("Course Name" ,text="Course Name")
        table.heading("Grades", text= "Grades")
        table.heading("Roll Number", text= "Roll Number")
        
        table.column("CourseID", width=120, anchor=CENTER)
        table.column("Course Name", width=250, anchor=W)
        table.column("Grades", width=100, anchor=CENTER)
        table.column("Roll Number", width=100, anchor=CENTER)
        cursor = get_cursor()
        cursor.execute(f"SELECT cs.courseId, c.courseName, cs.rollNumber, cs.grade FROM CoursesStatus as cs INNER JOIN Courses as c ON cs.courseId = c.courseId where cs.rollNumber = {self.rollNum}")        
        result = cursor.fetchall()
        for row in result:
            table.insert('', 'end', values=row)
            
        table.pack(fill= "both")
    
    def __std_pannel(self):
        from studentPannel import StudentPannel
        self.change_sc_fun(StudentPannel(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3",self.rollNum), self)

        