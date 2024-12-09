from tkinter import *
from tkinter import font
from tkinter import messagebox
from teacherpannel import TeacherPannel


class TeacherSignIn(Frame):
    
    def __init__(self, master, width, height, change_sc_fun,bg):
        Frame.__init__(self, master, width=width, height=height, bg= bg)
        self.change_sc_fun = change_sc_fun
        self.master = master
        self.width = width
        self.height = height
        self._init_teachUI()
        
    def _init_teachUI(self):
     customFontPath= "D:/eduplanner/fonts/Montserrat"
     customFont = font.Font(family= customFontPath, weight= 'bold' , size= 26)
     topBar = Label(self, bg='#AB886D', width=self.width, height=7) 
     text = Label(topBar , text= "TEACHER'S PORTAL", font= customFont, background= '#AB886D', foreground='#420e0b')
     text.place(x= 100, y= 44)
     backButtonPath = 'D:/eduplanner/assets/images/backButton1.png'
     self.backButton = PhotoImage(file=backButtonPath)
     self.backButton = self.backButton.subsample(7,8)
     backButton = Button(topBar, image= self.backButton, height=50, width=50, command = self.__auth_Screen, takefocus= False)
     backButton.place(x= 15, y= 33)
     topBar.pack()
     customFont1 = font.Font(family= customFontPath, weight= 'bold' , size= 15)
     
     id = Label( self , text= 'Enter Your ID', font =customFont1, foreground = '#420e0b', width= 20, height= 2, bg = "#D6C0B3")
     id.pack()
     idField = Entry(self, width= 40, foreground= "#420e0b")
     idField.pack(pady=10, ipady=20)
     
     password = Label(self, text="Enter Your Password", font= customFont1, foreground="#420e0b", width= 20, height= 2, bg= "#D6C0B3")
     password.pack(side='top')
     password_Field = Entry(self, width= 40, foreground= "#420e0b")
     password_Field.pack(pady=10, ipady=20)
     
     login = Button(self, text="Log In", width= 20, height= 1, bg= '#AB886D', command= lambda: self.__auth_teacher(idField.get(), password_Field.get()))
     login.pack()
     create = Label(self,text="create account",width= 20, height= 2, bg='#D6C0B3')
     create.pack()
     sign_in = Button(self, text= "SIGN UP", width= 20, height= 1, command= self.__sign_up, bg = '#AB886D')
     sign_in.pack()
     
  
     
    
    def __auth_Screen(self):
        from auth import Auth
        self.change_sc_fun(Auth(self.master, self.width, self.height, self.change_sc_fun), self)
        
    def __sign_up(self):
        from teacherregistration import Teacherregistration
        self.change_sc_fun(Teacherregistration(self.master, self.width, self.height, self.change_sc_fun,'#AB886D'), self)
        
    def __auth_teacher(self, id, password):
        if id=='' or password == '':
            messagebox.showerror("Error", "Fill all the fields")
            return
        from db import conn
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT pass FROM Auth WHERE acctype like 'F%' AND rollNo ={id} ")
        result = cursor.fetchall()
        if len(result) == 0:
            print("User ID not found")
            return
        if result[0][0] == password:
            self.change_sc_fun(TeacherPannel(self.master, self.width, self.height, self.change_sc_fun ,"#D6C0B3"),self)
        else:
            messagebox.showerror("Error", "Invalid Password")
            return
        
   
    
    