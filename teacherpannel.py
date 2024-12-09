from tkinter import *
from tkinter import font
from addcourse import AddCourse
from grading import TeacherGrading
from viewtables import ViewTable

class TeacherPannel(Frame):
    
    def __init__(self, master, width, height, change_sc_fun, bg):
         Frame.__init__(self, master, width=width, height=height, bg= bg)
         self.change_sc_fun = change_sc_fun
         self.master = master
         self.width = width
         self.height = height
         self.__init__porta1l()
        
    def __init__porta1l(self):
            customFontPath= "D:/eduplanner/fonts/Montserrat"
            customFont = font.Font(family= customFontPath, weight= 'bold' , size= 26)
            topBar = Label(self, bg='#AB886D', width= self.width, height=8) 
            text = Label(topBar , text= "TEACHER'S PORTAL ", font= customFont, background= '#AB886D', foreground='#420e0b')
            text.place(x= 100, y= 44)
            backButtonPath = 'D:/eduplanner/assets/images/backButton1.png'
            self.backButton = PhotoImage(file=backButtonPath)
            self.backButton = self.backButton.subsample(7,8)
            backButton = Button(topBar, image= self.backButton, height=50, width=50, command = self.__auth_Screen, takefocus= False)
            backButton.place(x= 15, y= 33)
            topBar.pack()
            button_color = "#4e2c13"
            button_text_color = "#ffffff"
            button1 = Button(self, command= self.__set_pre_req ,text="SET PREREQUISITE", bg=button_color, 
                    fg=button_text_color, font=(customFontPath, 12, "bold"),width= 31, height= 3, 
                    relief="flat")
            button1.pack()
            button2 =Button(self, text="VIEW COURSES & PRE REQUISITE ",command= self.__view_table , bg=button_color, 
                    fg=button_text_color, font=(customFontPath, 12, "bold"), width= 31, height= 3,
                    relief="flat")
            button2.pack()
            button3 =Button(self, text="ADD COURSE",command= self.__add_course , bg=button_color,width= 31, height= 3, 
                    fg=button_text_color, font=(customFontPath, 12, "bold"), 
                    relief="flat")
            button3.pack()
            
            button3 =Button(self, text="GRADE COURSE",command= self.__grade_course , bg=button_color,width= 31, height= 3, 
                    fg=button_text_color, font=(customFontPath, 12, "bold"), 
                    relief="flat")
            button3.pack()


    def __auth_Screen(self):
            from auth import Auth
            self.change_sc_fun(Auth(self.master, self.width, self.height, self.change_sc_fun), self)
    def __add_course(self):
        self.change_sc_fun(AddCourse(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3"), self)
            
    def __view_table(self):
        self.change_sc_fun(ViewTable(self.master, self.width, self.height, self.change_sc_fun, "#D6C0B3"), self)

    def __set_pre_req(self):
        from setprerequisite import SetPrequisite
        self.change_sc_fun(SetPrequisite(self.master, self.width, self.height, self.change_sc_fun, "#D6C0B3"), self)
        
    def __grade_course(self):
        self.change_sc_fun(TeacherGrading(self.master, self.width, self.height, self.change_sc_fun, "#D6C0B3"), self)
            

        