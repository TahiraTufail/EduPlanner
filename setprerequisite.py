from tkinter import *
from tkinter import messagebox
from tkinter import font
from db import get_cursor

class SetPrequisite(Frame):
    def __init__(self, master, width, height, change_sc_fun, bg):
        Frame.__init__(self, master, width=width, height=height, bg=bg)
        self.change_sc_fun = change_sc_fun
        self.master = master
        self.width = width
        self.height = height
        self.main_course = None  # To keep track of the main course when navigating back

        # Initialize UI
        self.__init_top_bar()
        self.__init_preReq()

    def __init_top_bar(self):
        customFontPath= "D:/eduplanner/fonts/Montserrat"
        customFont = font.Font(family= customFontPath, weight= 'bold' , size= 26)
        topBar = Label(self, bg='#AB886D', width= self.width, height=8) 
        text = Label(topBar , text= "SET PREREQUISITE ", font= customFont, background= '#AB886D', foreground='#420e0b')
        text.place(x= 100, y= 44)
        backButtonPath = 'D:/eduplanner/assets/images/backButton1.png'
        self.backButton = PhotoImage(file=backButtonPath)
        self.backButton = self.backButton.subsample(7,8)
        backButton = Button(topBar, image= self.backButton, height=50, width=50, command = self.__teacher_pannel, takefocus= False)
        backButton.place(x= 15, y= 33)
        topBar.pack()

    def __init_preReq(self):
        """Initialize the prerequisite courses display."""
        container = Frame(self,bg='#AB886D', height= 700, padx=10, pady= 10 )
        container.pack(ipadx= 129, ipady= 90)

        canvas = Canvas(container)
        scrollbar = Scrollbar(container,border=9,width= 25, borderwidth=15, activebackground='#AB886D', orient=VERTICAL, command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        courses = self.__get_courses()
        for idx, course in enumerate(courses):
            self.__create_course(course, idx, command=self.__set_preReq, args=[course])

    def __get_courses(self, exclude=None):
        """Fetch courses from the database, optionally excluding a specific course."""
        cursor = get_cursor()
        if exclude:
            cursor.execute(
                f"SELECT courseId, courseName FROM Courses WHERE courseName != '{exclude}'"
            )
        else:
            cursor.execute("SELECT courseId, courseName FROM Courses")
        courses = cursor.fetchall()
        return courses

    def __create_course(self, course, index, command, args):
        """Create a list item for a course."""
        course_frame = Frame(self.scrollable_frame, bg="#AB886D", relief=RAISED)
        course_frame.pack()

        course_label = Label(course_frame, text=course[1], anchor="w", width=70, bg="pink")
        course_label.pack(side=LEFT, padx=10, pady=5)

        select_button = Button(
            course_frame, text="Select", command=lambda: self.__highlight_selection(course_frame, command, *args),bg='#AB886D',width= 10
        )
        select_button.pack(side=RIGHT, padx=10, pady=5)

    def __highlight_selection(self, course_frame, command, *args):
        """Highlight the selected row and execute the command."""
        for child in self.scrollable_frame.winfo_children():
            if isinstance(child, Frame):
                child.configure(bg="#D6C0B3")

        course_frame.configure(bg="lightgreen")
        self.main_course = args[0]  # Save the main course for navigation
        command(*args)

    def clear_frame(self):
        """Clear all widgets in the frame."""
        for widget in self.winfo_children():
            widget.destroy()

    def __add_preReq(self, main_course, pre_req):
        """Add a prerequisite course to the database."""
        cursor = get_cursor()
        cursor.execute(
            f"INSERT INTO PreReq (courseId, preReqCourseId) VALUES ({main_course[0]}, {pre_req[0]})"
        )
        cursor.commit()
        messagebox.showinfo("Success", "Successfully added")

    def __set_preReq(self, main_course):
        """Display courses to select as prerequisites for the main course."""
        self.clear_frame()
        self.__init_top_bar()

        container = Frame(self)
        container.pack(fill=BOTH, expand=True)

        canvas = Canvas(container)
        scrollbar = Scrollbar(container, orient=VERTICAL, command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        courses = self.__get_courses(exclude=main_course[1])
        for idx, course in enumerate(courses):
            self.__create_course(course, idx, command=self.__add_preReq, args=[main_course, course])

    def __back_to_main_courses(self):
        """Navigate back to the main course selection."""
        self.clear_frame()
        self.__init_top_bar()
        self.__init_preReq()
        
    def __teacher_pannel(self):
        from teacherpannel import TeacherPannel
        self.change_sc_fun(TeacherPannel(self.master, self.width, self.height, self.change_sc_fun,"#D6C0B3"), self)