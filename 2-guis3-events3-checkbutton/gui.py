from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        self.title("Passport checker")

        self.__add_main_heading()
        self.__add_heading_match_face()
        self.__add_heading_validity_date()
        self.__add_heading_visa_valid()
        self.__add_first_yes()
        self.__add_first_no()
        self.__add_second_yes()
        self.__add_second_no()
        self.__add_third_yes()
        self.__add_third_no()
        self.__add_button()

    def __add_main_heading(self):
        self.main_heading = Label()
        self.main_heading.grid(row=0, column=0)
        self.main_heading.configure(text="Passport Checker", font="Arial 24", fg="#000")

    def __add_heading_match_face(self):
        self.heading_match_face = Label()
        self.heading_match_face.grid(row=1, column=0, sticky=W)
        self.heading_match_face.configure(text="1. Photo matches face?", font="Arial 16", fg="#000")

    def __add_first_yes(self):
        pass

    def __add_first_no(self):
        pass




    def __add_heading_validity_date(self):
        self.heading_validity_date = Label()
        self.heading_validity_date.grid(row=2, column=0, sticky=W)
        self.heading_validity_date.configure(text="2. Passport has at least 6 months validity?", font="Arial 16", fg="#000")

    def __add_second_yes(self):
        pass

    def __add_second_no(self):
        pass




    def __add_heading_visa_valid(self):
        self.heading_visa_valid = Label()
        self.heading_visa_valid.grid(row=3, column=0, sticky=W)
        self.heading_visa_valid.configure(text="3. Visa, if required, is valid?", font="Arial 16", fg="#000")

    def __add_third_yes(self):
        pass

    def __add_third_no(self):
        pass





    def __add_button(self):
        self.button = Button()
        self.button.grid(row=4, column=0)
        self.button.configure(text="Add", font="Arial 16", padx=20)       
