from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.umbrella_image = PhotoImage(file="umbrella.gif")
        
        # set window attributes
        self.configure(height=1000, width=1000)

        # set animation attributes
        self.umbrella_x_position = 250
        self.umbrella_y_position = 50
        self.umbrella_x_change = 5
        self.umbrella_y_change= 5
        
        # add components
        self.add_umbrella_image_label()
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):

        if self.umbrella_x_position >= 500:
            self.umbrella_x_change = self.umbrella_x_change * -1

        if self.umbrella_y_position >= 500:
            self.umbrella_y_change = self.umbrella_y_change * -1

        if self.umbrella_y_position <= 0:
            self.umbrella_y_change = self.umbrella_y_change * -1

        if self.umbrella_x_position <= 0:
            self.umbrella_x_change = self.umbrella_x_change * -1
        
        self.umbrella_x_position = self.umbrella_x_position + self.umbrella_x_change
        self.umbrella_y_position = self.umbrella_y_position + self.umbrella_y_change
        self.umbrella_image_label.place(x=self.umbrella_x_position, y=self.umbrella_y_position)
        self.after(100, self.tick)

    # the ball image
    def add_umbrella_image_label(self):
        self.umbrella_image_label = Label()
        self.umbrella_image_label.place(x=self.umbrella_x_position, y=self.umbrella_y_position)
        self.umbrella_image_label.configure(image=self.umbrella_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
