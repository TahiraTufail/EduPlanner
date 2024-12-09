from tkinter import *



class StudentPannel(Frame):
    
    def __init__(self, master, width, height, change_sc_fun, bg,rollNum):
         Frame.__init__(self, master, width=width, height=height, bg= bg)
         self.change_sc_fun = change_sc_fun
         self.master = master
         self.width = width
         self.height = height
         self.rollNum = rollNum
         self.__init__portal()
        
    def __init__portal(self):
            header = Label(self, text="STUDENT PORTAL", bg="#AB886D", fg="#4e2c13", 
                  font=("Arial", 16, "bold"), anchor="w")
            header.place(x=10, y=10, width=750, height=50)

# Button Styles
            button_color = "#4e2c13"
            button_text_color = "#ffffff"

# Buttons
            button1 = Button(self, command= self.__course_enrollment,text="Course Enrollment", bg=button_color, 
                    fg=button_text_color, font=("Arial", 12, "bold"), 
                    relief="flat")
            button1.place(x=200, y=200, width=350, height=50)
            button2 = Button(self, text="VIEW YOUR GRADES", command= self.__view_grades, bg=button_color,fg=button_text_color, font=("Arial", 12, "bold"), 
                    relief="flat" )
            button2.place(x=200, y= 280, width= 350, height= 50)
            button3 =Button(self, text="View Registered Courses",command=self.__view_table, bg=button_color, 
                    fg=button_text_color, font=("Arial", 12, "bold"), 
                    relief="flat")
            button3.place(x=200, y=360, width=350, height=50)

        
        
    def __course_enrollment(self):
         from studentenrollment import StudentEnrollment

         self.change_sc_fun(StudentEnrollment(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3",self.rollNum), self)
         
    def __view_table(self):
         from studentcourseview import Stdcourseview
         self.change_sc_fun(Stdcourseview(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3",self.rollNum), self)
    def __view_grades(self):
         from viewgrades import ViewGrades     
         self.change_sc_fun(ViewGrades(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3",self.rollNum), self)
                


        