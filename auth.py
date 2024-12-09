from tkinter import *
from studentsignin import StudentSignIn
from teachersignin import TeacherSignIn
from tkinter import font 

# __(variable name)__()  These methods are special methods of a class known as dunder methods.
# They are used for operator overloading, class attribute initialization and many other special tasks

class Auth(Frame):
    
    def __init__(self, master, width, height, change_sc_fun ):
        Frame.__init__(self, master, width=width, height=height, bg= "#D6C0B3")
        self.change_sc_fun = change_sc_fun
        self.master = master
        self.width = width
        self.height = height
        self.__initUI()
  
    
    def __initUI(self):
        customPath = "D:/eduplanner/fonts/Montserrat"
        customfont= font.Font(family= customPath, size=10, weight= 'bold', slant= 'roman')
        img = PhotoImage(file="./assets/images/logo.png")
        img= img.subsample(2,2)
        image = Label(self, image=img)
        image.image = img
        image.place(x= 254 , y= 60)
        stdButton = Button(self, text= "LOGIN AS STUDENT", bg= "#AB886D" , width= 31, height= 2, command= self.__student_signIn, font= customfont, foreground= '#420e0b')
        stdButton.place(x= 254, y= 300)
        teacherButton = Button(self, text= "LOGIN AS TEACHER", bg= "#AB886D" , width= 31, height= 2, command= self.__teacher_signIn, font= customfont, foreground= '#420e0b')
        teacherButton.place(x= 254, y= 380)
        
        
    def __student_signIn(self):
        self.change_sc_fun(StudentSignIn(self.master,self.width, self.height, self.change_sc_fun, "#D6C0B3"), self)
   
    def __teacher_signIn(self):
        self.change_sc_fun(TeacherSignIn(self.master,self.width, self.height, self.change_sc_fun, "#D6C0B3" ), self)
        
        