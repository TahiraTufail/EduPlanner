from tkinter import *
from tkinter import font
from tkinter import messagebox
from db import get_cursor


class AddCourse(Frame):
    
    def __init__(self, master, width, height, change_sc_fun, bg):
        Frame.__init__(self, master, width=width, height=height, bg= bg)
        cursor = get_cursor()
        cursor.execute("SELECT TOP 1 courseId from Courses order by courseId desc")
        result = cursor.fetchone()
        if result is not None:
            self.courseId = result[0] + 1
        else:
            self.courseId = 0
            
        self.change_sc_fun = change_sc_fun
        self.master = master
        self.width = width
        self.height = height
        self.__init__UI()
    
    def __init__UI(self):
        font1 = "D:/eduplanner/fonts/Montserrat"
        customFont = font.Font(family= font1, weight= 'bold' , size= 26)
        normalfont = font.Font(family= font1, weight= 'normal' , size= 18)
        topBar = Label(self, bg='#AB886D', width= self.width, height=8) 
        text = Label(topBar , text= "ADD COURSE ", font= customFont, background= '#AB886D', foreground='#420e0b')
        text.place(x= 100, y= 44)
        backButtonPath = 'D:/eduplanner/assets/images/backButton1.png'
        self.backButton = PhotoImage(file=backButtonPath)
        self.backButton = self.backButton.subsample(7,8)
        backButton = Button(topBar, image= self.backButton, height=50, width=50, command = self.__auth_Screen, takefocus= False)
        backButton.place(x= 15, y= 33)
        topBar.place(x=0, y=0 )
        courseName = Label(self, text="COURSE NAME", font= font1, width= 20, height=3, anchor= 'center', bg= '#AB886D', foreground= '#420e0b' )
        courseName.place(x= 10, y= 240)
        courseNamefi = Entry(self, bg= '#AB886D', justify= 'center',width= 20, font= normalfont)
        courseNamefi.place(x= 250, y= 260)
        credit_hr= Label(self, text="CREDIT HR.", font= font1, width= 20, height=3, anchor='center', bg= "#AB886D", foreground= "#420e0b")
        credit_hr.place(x= 10, y= 440)
        credit_hrfi = Entry(self, bg= '#AB886D', justify= 'center',width= 20, font= normalfont)
        credit_hrfi.place(x= 250, y= 460)
        saveButton = Button(text= "save changes", height= 4, width=25, bg= '#AB886D', foreground= '#420e0b', command= lambda: self.__add_course(courseNamefi.get(),credit_hrfi.get()  ))
        saveButton.place(x= 580, y= 520)
        
        
        
    def __auth_Screen(self):
        from teacherpannel import TeacherPannel
        self.change_sc_fun(TeacherPannel(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3"), self)
    
    def __add_course(self, courseName, credithr):
        cursor = get_cursor()
        cursor.execute(f"INSERT INTO Courses (courseId, courseName, creditHour) VALUES ({self.courseId} ,'{courseName}' , {credithr})")
        cursor.commit()
        self.courseId +=1
        messagebox.showinfo('Success',f'Sucessfully added {courseName}')
            
            
            
            