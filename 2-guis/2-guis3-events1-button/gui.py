from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
    def __add_heading_label(self):
        # create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        # style
        self.heading_label.configure(text="Buy Tickets", font="Arial 24", fg="#000")
        
    def __add_instruction_label(self):
        # create
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0, sticky=W, padx=10)
        # style
        self.instruction_label.configure(text="How many tickets are needed?", font="Arial 16", fg="#000")
        
    def __add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=2, column=0, sticky=N+E+S+W, padx=10, pady=5)
        self.tickets_entry.configure(text="No. of tickets", font="Arial 16", bd=2)
        
    def __add_buy_button(self):
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0, pady=10)
        # style
        self.buy_button.configure(text="Buy", font="Arial 16", borderwidth=2, relief="groove", width="10")

        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)

    def __buy_button_clicked(self, event):
         messagebox.showinfo("Purchased!", "You have purchased the tickets!")
