from tkinter  import*
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import Combobox
from auth import Auth
from db import get_cursor


class Teacherregistration(Frame):
    def __init__(self, master, width, height, change_sc_fun, bg):
        Frame.__init__(self, master, width=width, height=height, bg= bg)
        self.change_sc_fun = change_sc_fun
        self.master = master
        self.width = width
        self.height = height
        self.__init__coursereg()
    
    def __init__coursereg(self):
        customFontPath= "D:/eduplanner/fonts/Montserrat"
        customFont = font.Font(family= customFontPath, weight= 'bold' , size= 26)
        topBar = Label(self, bg='#AB886D', width= self.width, height=8) 
        text = Label(topBar , text= "TEACHER'S PORTAL", font= customFont, background= '#AB886D', foreground='#420e0b')
        text.place(x= 100, y= 44)
        backButtonPath = 'D:/eduplanner/assets/images/backButton1.png'
        self.backButton = PhotoImage(file=backButtonPath)
        self.backButton = self.backButton.subsample(7,8)
        backButton = Button(topBar, image= self.backButton, height=50, width=50, command = self.__backButton, takefocus= False)
        backButton.place(x= 15, y= 33)
        topBar.pack(fill= 'both')
                # Form fields
        formFrame = Frame(self, bg='white', padx=60, pady=140)
        formFrame.pack()
        #rollnumber
        Label(formFrame, text="TeacherId", bg='white', font=('Arial', 12)).grid(row=0, column=0, pady=5, sticky=W)
        self.rollNum= Entry(formFrame, font=('Arial', 12), width=30)
        self.rollNum.grid(row=0, column=1, pady=5, padx=10)
        #password
        Label(formFrame, text="Password:", bg='white', font=('Arial', 12)).grid(row=1, column=0, pady=5, sticky=W)
        self.passwordEntry = Entry(formFrame, font=('Arial', 12), width=30, show="*")  # Masking the password field
        self.passwordEntry.grid(row=1, column=1, pady=5, padx=10)
        # Name field
        Label(formFrame, text="First Name:", bg='white', font=('Arial', 12)).grid(row=2, column=0, pady=5, sticky=W)
        self.firstnameEntry = Entry(formFrame, font=('Arial', 12), width=30)
        self.firstnameEntry.grid(row=2, column=1, pady=5, padx=10)
        
        Label(formFrame, text="Last Name:", bg='white', font=('Arial', 12)).grid(row=3, column=0, pady=5, sticky=W)
        self.lastnameEntry = Entry(formFrame, font=('Arial', 12), width=30)
        self.lastnameEntry.grid(row=3, column=1, pady=5, padx=10)
        
        Label(formFrame, text="Designation", bg='white', font=('Arial', 12)).grid(row=4, column=0, pady=5, sticky=W)
        self.designationEntry = Entry(formFrame, font=('Arial', 12), width=30)
        self.designationEntry.grid(row=4, column=1, pady=5, padx=10)
        
        
        # Save button
        saveButton = Button(formFrame, text="Next", font=('Arial', 12), bg='#AB886D', fg='white', command=self.__save_changes)
        saveButton.grid(row=7, column=0, columnspan=2, pady=20)

    def __backButton(self):
        self.change_sc_fun(Auth(self.master, self.width, self.height, self.change_sc_fun), self)

    def __save_changes(self):
        rollNum = self.rollNum.get()
        password= self.passwordEntry.get()
        fname = self.firstnameEntry.get()
        lname = self.lastnameEntry.get()
        designation = self.designationEntry.get()
        acctype = "Faculty"
        cursor = get_cursor()
        cursor.execute(f"INSERT INTO Teacher (teacherId, teacherfirstName, teacherLastName, designation) VALUES ({rollNum}, '{fname}', '{lname}', '{designation}')")
        cursor.commit()
        messagebox.showinfo("success", "Sucessfully Added" )
        cursor.execute(f"INSERT INTO Auth (rollNo,pass,acctype) VALUES ({rollNum}, '{password}', '{acctype}')").commit()
          
    def __backButton(self):
        self.change_sc_fun(Auth(self.master, self.width, self.height, self.change_sc_fun), self)
        
            
        
        
        
        
        
        
      