# import all classes the tkinter libirary
from tkinter import *

# class defenition for your Gui
class Gui(Tk):

    # constructor for making Gui objects
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="#404040", height=1000, width=1000)

        # add components to the window
        self.__add_heading_label()
        self.__add_subheading_label()
        self.__add_email_label()
        self.__add_user_entry()
        self.__add_button()

    def __add_heading_label(self):
        # create
        self.heading_label = Label()
        self.heading_label.place(x=0, y=0)
        # style
        self.heading_label.configure(text="Recieve out newsletter", bg="#404040", font="Arial 32 underline", fg="#fff", padx=5, pady=5)
        # handle events
        
    def __add_subheading_label(self):
        self.subheading_label = Label()
        self.subheading_label.place(x=5, y=100)
        # style
        self.subheading_label.configure(text="Please enter your email address to recieve our news letter", bg="#404040", font="Arial 18 bold", fg="#fff", padx=5, pady=5)

    def __add_email_label(self):
        self.email_label = Label()
        self.email_label.place(x=5, y=150)
        # style
        self.email_label.configure(text="Email:", bg="#404040", font="Arial 16", fg="#fff")

    def __add_user_entry(self):
        self.user_entry = Entry()
        self.user_entry.place(x=80, y=150)
        # style
        self.user_entry.configure(fg="#404040", font="Arial 16", bd=5)

    def __add_button(self):
        self.button = Button()
        self.button.place(x=5, y=200)
        # style
        self.button.configure(fg="#404040", text="Subscribe", font="Arial 16", bd=5, cursor="dot", width=50)
