from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
    	 # load resources
        self.tick_image = PhotoImage(file="tick.gif")
        self.cross_image = PhotoImage(file="cross.gif")
        
        # set window attributes
        self.title("Gui")
        self.configure(width=1000, height=1000)
        
        # add components
        self.__add_main_heading_label()
        self.__add_name_label()
        self.__add_name_box()
        self.__add_name_entered()
        self.__add_passport_label()
        self.__add_passport_box()
        self.__add_passport_entered()
        self.__add_nights_label()
        self.__add_nights_box()
        self.__add_nights_entered()
        
    def __add_main_heading_label(self):
        self.main_heading_label = Label()
        self.main_heading_label.grid(row=0, columnspan=3)
        self.main_heading_label.configure(text="Hotel Check In", font="Arial 24")

    def __add_name_label(self):
        self.main_heading_label = Label()
        self.main_heading_label.grid(row=1, column=0)
        self.main_heading_label.configure(text="Name:", font="Arial 18")

    def __add_name_box(self):
        self.name_box = Entry()
        self.name_box.grid(row=1, column=1)
        self.name_box.bind("<KeyRelease>", self.name_box_entry)

    def name_box_entry(self, event):
        name = self.name_box.get()
        if len(name) == 0:
            self.name_entered.configure(image=self.cross_image)
        else:
            self.name_entered.configure(image=self.tick_image)
        
    def __add_name_entered(self):
        self.name_entered = Label()
        self.name_entered.grid(row=1, column=2)
        self.name_entered.configure(image=self.cross_image, height=24, width=24, bd=2, relief="solid")


        
        
    def __add_passport_label(self):
        self.passport_label = Label()
        self.passport_label.grid(row=2, column=0)
        self.passport_label.configure(text="Passport Number", font="Arial 18")
        
    def __add_passport_box(self):
        self.passport_box = Entry()
        self.passport_box.grid(row=2, column=1)
        self.passport_box.bind("<KeyRelease>", self.name_passport_entry)
        
    def __add_passport_entered(self):
        self.passport_entered = Label()
        self.passport_entered.grid(row=2, column=2)
        self.passport_entered.configure(image=self.cross_image, height=24, width=24, bd=2, relief="solid")

    def name_passport_entry(self, event):
        name = self.passport_box.get()
        if len(name) == 0:
            self.passport_entered.configure(image=self.cross_image)
        else:
            self.passport_entered.configure(image=self.tick_image)


        
                
    def __add_nights_box(self):
        self.nights_box = Entry()
        self.nights_box.grid(row=3, column=1)

    def __add_nights_label(self):
        self.nights_label = Label()
        self.nights_label.grid(row=3, column=0)
        self.nights_label.configure(text="No. of nights", font="Arial 18")
        
    def __add_nights_box(self):
        self.nights_box = Entry()
        self.nights_box.grid(row=3, column=1)
        self.nights_box.bind("<KeyRelease>", self.name_nights_entry)
        
    def __add_nights_entered(self):
        self.nights_entered = Label()
        self.nights_entered.grid(row=3, column=2)
        self.nights_entered.configure(image=self.cross_image, height=24, width=24, bd=2, relief="solid")

    def name_nights_entry(self, event):
        name = self.nights_box.get()
        if len(name) == 0:
            self.nights_entered.configure(image=self.cross_image)
        else:
            self.nights_entered.configure(image=self.tick_image)
            

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
