from tkinter import *
from auth import Auth
from db import close_connection

def switch_screen(new_screen, old_screen = None):
    if old_screen != None:
        old_screen.destroy()
    new_screen.pack()
    
app = Tk()
app.geometry("750x600")
app.title("EduPlanner")
app.maxsize(750,600)
app.minsize(750,600)
# Screens
auth = Auth(app, 750, 600, switch_screen)
# Initial Screen
switch_screen(auth)
app.mainloop()

close_connection()