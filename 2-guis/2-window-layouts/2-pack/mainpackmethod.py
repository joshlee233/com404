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
        self.__add_main_frame()
        self.__add_heading_label()
        self.__add_subheading_label()
        self.__add_email_frame()
        self.__add_email_label()
        self.__add_user_entry()
        self.__add_button()

    def __add_main_frame(self):
        self.main_frame = Frame()
        self.main_frame.pack()

    def __add_heading_label(self):
        # create
        self.heading_label = Label(self.main_frame)
        self.heading_label.pack(fill=X)
        # style
        self.heading_label.configure(text="Recieve out newsletter", bg="#404040", font="Arial 32 underline", fg="#fff", padx=5, pady=5)
        # handle events
        
    def __add_subheading_label(self):
        self.subheading_label = Label(self.main_frame)
        self.subheading_label.pack(fill=X)
        # style
        self.subheading_label.configure(text="Please enter your email address to recieve our news letter", bg="#404040", font="Arial 18 bold", fg="#fff", padx=5, pady=5)

    def __add_email_frame(self):
        self.email_frame = Frame(self.main_frame)
        self.email_frame.pack(fill=X)
        self.email_frame.configure(bg="#404040", padx=10, pady=10)

    def __add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side=LEFT)
        # style
        self.email_label.configure(text="Email:", bg="#404040", font="Arial 16", fg="#fff", padx=20)

    def __add_user_entry(self):
        self.user_entry = Entry(self.email_frame)
        self.user_entry.pack(side=LEFT)
        # style
        self.user_entry.configure(fg="#404040", font="Arial 16", bd=2)

    def __add_button(self):
        self.button = Button(self.main_frame)
        self.button.pack(fill=X)
        # style
        self.button.configure(fg="#404040", text="Subscribe", font="Arial 16", bd=5, cursor="dot", width=50)
