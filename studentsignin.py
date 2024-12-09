from tkinter import *
from tkinter import font
from tkinter import messagebox
from studentPannel import StudentPannel

class StudentSignIn(Frame):
    
    def __init__(self, master, width, height, change_sc_fun, bg):
        Frame.__init__(self, master, width=width, height=height, bg= bg)
        self.change_sc_fun = change_sc_fun
        self.master = master
        self.width = width
        self.height = height
        
        self. _init_stdUI()
        
    def _init_stdUI(self):
        customFontPath= "D:/eduplanner/fonts/Montserrat"
        customFont = font.Font(family= customFontPath, weight= 'bold' , size= 26)
        topBar = Label(self, bg='#AB886D', width= self.width, height=8) 
        text = Label(topBar , text= "STUDENT'S PORTAL ", font= customFont, background= '#AB886D', foreground='#420e0b')
        text.place(x= 100, y= 44)
        backButtonPath = 'D:/eduplanner/assets/images/backButton1.png'
        self.backButton = PhotoImage(file=backButtonPath)
        self.backButton = self.backButton.subsample(7,8)
        backButton = Button(topBar, image= self.backButton, height=50, width=50, command = self.__auth_Screen, takefocus= False)
        backButton.place(x= 15, y= 33)
        topBar.pack()
        
        customFont1 = font.Font(family= customFontPath, weight= 'bold' , size= 15)
        
        id = Label( self , text= 'Enter Your ID', font =customFont1, foreground = '#420e0b', width= 16, height= 2, bg = "#D6C0B3")
        id.pack(padx= 12, pady= 10)
        idField = Entry(self, width= 40, foreground= "#420e0b")
        idField.pack(pady=12,ipady= 8)
        
        password = Label(self, text="Enter Your Password", font= customFont1, foreground="#420e0b", width= 16, height= 2, bg= "#D6C0B3")
        password.pack(padx=12 ,pady= 10)
        password_Field = Entry(self, width= 40, foreground= "#420e0b")
        password_Field.pack(ipady=8, pady=12)
        
        login = Button(self, text="Log In", width= 20, height= 2, bg= '#AB886D', command= lambda: self.__authenticate_user(idField.get(), password_Field.get()))
        login.pack(pady= 18)
        create = Label(self,text="create account",width= 20, height= 2, bg='#D6C0B3')
        create.pack()
        sign_up = Button(self, text="Sign Up", width=10, height=1, bg='#AB886D', command=self.__sign_up)
        sign_up.pack()
        

    def __auth_Screen(self):
        from auth import Auth
        self.change_sc_fun(Auth(self.master, self.width, self.height, self.change_sc_fun), self)
    
    def __sign_up(self):
        from stdregistration import Stdregistration
        self.change_sc_fun(Stdregistration(self.master, self.width, self.height, self.change_sc_fun, '#D6C0B3'), self)
        
     
    def __authenticate_user(self, id, password):
        if id=='' or password=='':
            messagebox.showerror("Error", "Please fill all the fields")
            return
        from db import conn
        cursor = conn.cursor()
        cursor.execute(f"SELECT pass FROM Auth WHERE acctype like 's%' AND rollNo = {id} ")
        result = cursor.fetchall()
        rollNum = cursor.execute(f"SELECT rollNo FROM Auth WHERE rollNo = {id}").fetchall()
        if len(result)== 0:
            messagebox.showerror("Error", "Invalid ID")
            return
        if result[0][0] == password:
            messagebox.showinfo("Success", "You Logged in successfully")
            self.change_sc_fun(StudentPannel(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3",id), self)
            
        else:
            messagebox.showerror("Error", "Invalid Password")
            return