from tkinter import *
from tkinter import messagebox

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
        self.__add_check_button()

    def __add_main_heading(self):
        self.main_heading = Label()
        self.main_heading.grid(row=0, column=0)
        self.main_heading.configure(text="Passport Checker", font="Arial 24", fg="#000")

    def __add_heading_match_face(self):
        self.heading_match_face = Label()
        self.heading_match_face.grid(row=1, column=0, sticky=W)
        self.heading_match_face.configure(text="1. Photo matches face?", font="Arial 16", fg="#000")




    def __add_first_yes(self):
        self.first_yes_value = IntVar()
        
        self.first_yes = Checkbutton(variable= self.first_yes_value)
        self.first_yes.grid(row=1, column=1, sticky=W)
        self.first_yes.configure(text="Yes?", font="Arial 14", fg="#000")
        
        self.first_yes.bind("<ButtonRelease-1>", self.__first_yes_clicked)

    def __first_yes_clicked(self,event):
        self.first_no.deselect()
        


        

    def __add_first_no(self):
        self.first_no = Checkbutton()
        self.first_no.grid(row=1, column=2, sticky=W)
        self.first_no.configure(text="No?", font="Arial 14", fg="#000")

        self.first_no.bind("<ButtonRelease-1>", self.__first_no_clicked)
        
        
    def __first_no_clicked(self,event):
        self.first_yes.deselect()
        




    def __add_heading_validity_date(self):
        self.heading_validity_date = Label()
        self.heading_validity_date.grid(row=2, column=0, sticky=W)
        self.heading_validity_date.configure(text="2. Passport has at least 6 months validity?", font="Arial 16", fg="#000")



    def __add_second_yes(self):
        self.second_yes_value = IntVar()
        
        self.second_yes = Checkbutton(variable= self.second_yes_value)
        self.second_yes.grid(row=2, column=1, sticky=W)
        self.second_yes.configure(text="Yes?", font="Arial 14", fg="#000")
        
        self.second_yes.bind("<ButtonRelease-1>", self.__second_yes_clicked)
        
    def __second_yes_clicked(self,event):
        self.second_no.deselect()
        

        

    def __add_second_no(self):
        self.second_no = Checkbutton()
        self.second_no.grid(row=2, column=2, sticky=W)
        self.second_no.configure(text="No?", font="Arial 14", fg="#000")

        self.second_no.bind("<ButtonRelease-1>", self.__second_no_clicked)
        
    def __second_no_clicked(self,event):
        self.second_yes.deselect()




    def __add_heading_visa_valid(self):
        self.heading_visa_valid = Label()
        self.heading_visa_valid.grid(row=3, column=0, sticky=W)
        self.heading_visa_valid.configure(text="3. Visa, if required, is valid?", font="Arial 16", fg="#000")



    def __add_third_yes(self):
        self.third_yes_value = IntVar()
        
        self.third_yes = Checkbutton(variable= self.third_yes_value)
        self.third_yes.grid(row=3, column=1, sticky=W)
        self.third_yes.configure(text="Yes?", font="Arial 14", fg="#000")
        
        self.third_yes.bind("<ButtonRelease-1>", self.__third_yes_clicked)
        
    def __third_yes_clicked(self,event):
        self.third_no.deselect()
        
        

    def __add_third_no(self):
        self.third_no = Checkbutton()
        self.third_no.grid(row=3, column=2, sticky=W)
        self.third_no.configure(text="No?", font="Arial 14", fg="#000")

        self.third_no.bind("<ButtonRelease-1>", self.__third_no_clicked)
        
    def __third_no_clicked(self,event):
        self.third_yes.deselect()





    def __add_check_button(self):
        self.check_button = Button()
        self.check_button.grid(row=4, column=0)
        self.check_button.configure(text="Check", font="Arial 16", padx=20)

        self.check_button.bind("<ButtonRelease-1>", self.__check_button_clicked)


    def __check_button_clicked(self,event):
        first_yes_value = self.first_yes_value.get()
        second_yes_value = self.second_yes_value.get()
        third_yes_value = self.third_yes_value.get()
        
        if (first_yes_value==1 and second_yes_value==1 and third_yes_value==1):
            messagebox.showinfo("Passport checker", "You have passed the check!")
        else:
            messagebox.showinfo("Passport checker","You failed the check!")
