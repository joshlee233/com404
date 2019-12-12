from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
    	 # load resources
        self.bus_image = PhotoImage(file="bus.gif")
        self.map_image = PhotoImage(file="map.gif")
        
        # set window attributes
        self.title("Gui")
        self.configure(height=500, width=500)
        
        # add components
        self.__add_main_heading_label()
        self.__add_map_frame()
        self.__add_map_image()
        self.__add_bus_image()

    def __add_main_heading_label(self):
        self.main_heading_label = Label()
        self.main_heading_label.place(x=0, y=0)
        self.main_heading_label.configure(text="Bus journey", font="Arial 24")

    def __add_map_frame(self):
        self.add_map_frame = Frame()
        self.add_map_frame.place(x=0, y=50)
        self.add_map_frame.configure(width=500, height=500)

    def __add_bus_image(self):
        self.add_bus_image = Label(self.add_map_frame)
        self.add_bus_image.place(x=0, y=0)
        self.add_bus_image.configure(image=self.bus_image, bd=2, relief="solid")

        self.add_bus_image.bind("<B1-Motion>", self.bus_move)
    
    def __add_map_image(self):
        self.add_map_image = Label(self.add_map_frame)
        self.add_map_image.place(x=0, y=0)
        self.add_map_image.configure(image=self.map_image, bd=2, relief="solid")

    def bus_move(self, event):
        self.add_bus_image.place(x=event.x, y=event.y)

    
        
# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
