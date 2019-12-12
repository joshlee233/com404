from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
    	 # load resources
        self.cactus_image_with = PhotoImage(file="cactusimagewith.gif")
        self.cactus_image_without = PhotoImage(file="cactusimagewithout.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_main_heading_label()
        self.__add_cactus_image()
        self.__add_flip_button()

    def __add_main_heading_label(self):
        self.main_heading_label = Label()
        self.main_heading_label.grid(row=0, columnspan=3)
        self.main_heading_label.configure(text="Transport", font="Arial 24")
    
    def __add_cactus_image(self):
        self.cactus_image = Label()
        self.cactus_image.grid(row=1, column=0)
        self.cactus_image.configure(image=self.cactus_image_without, height=500, width=500, bd=2, relief="solid")

    def __add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=2, columnspan=3)
        self.flip_button.configure(text="Flip",font="Arial 24" , bd=2, relief="solid")

        self.flip_button.bind("<ButtonRelease-1>", self.__button_click_left)
        self.flip_button.bind("<ButtonRelease-3>", self.__button_click_right)
        
    def __button_click_left(self, event):
        self.cactus_image.configure(image=self.cactus_image_without)
         
    def __button_click_right(self, event):
        self.cactus_image.configure(image=self.cactus_image_with)

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
