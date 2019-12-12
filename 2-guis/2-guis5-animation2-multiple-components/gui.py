from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_one_image = PhotoImage(file="ball1.gif")
        self.ball_two_image = PhotoImage(file="ball2.gif")
        
        # set window attributes
        self.configure(height=1000, width=1000)

        # set animation attributes
        self.ball_one_x_position = 250
        self.ball_one_y_position = 50
        self.ball_one_x_change = 5
        self.ball_one_y_change = 5

        self.ball_two_x_position = 250
        self.ball_two_y_position = 50
        self.ball_two_x_change = -5
        self.ball_two_y_change = -5
        
        # add components
        self.add_ball_one_image_label()
        self.add_ball_two_image_label()
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):

        if self.ball_one_x_position >= 500:
            self.ball_one_x_change = self.ball_one_x_change * -1

        if self.ball_one_y_position >= 500:
            self.ball_one_y_change = self.ball_one_y_change * -1

        if self.ball_one_y_position <= 0:
            self.ball_one_y_change = self.ball_one_y_change * -1

        if self.ball_one_x_position <= 0:
            self.ball_one_x_change = self.ball_one_x_change * -1
        
        self.ball_one_x_position = self.ball_one_x_position + self.ball_one_x_change
        self.ball_one_y_position = self.ball_one_y_position + self.ball_one_y_change
        self.ball_one_image_label.place(x=self.ball_one_x_position, y=self.ball_one_y_position)
               

        if self.ball_two_x_position >= 500:
            self.ball_two_x_change = self.ball_two_x_change * -1

        if self.ball_two_y_position >= 500:
            self.ball_two_y_change = self.ball_two_y_change * -1

        if self.ball_two_y_position <= 0:
            self.ball_two_y_change = self.ball_two_y_change * -1

        if self.ball_two_x_position <= 0:
            self.ball_two_x_change = self.ball_two_x_change * -1
        
        self.ball_two_x_position = self.ball_two_x_position + self.ball_two_x_change
        self.ball_two_y_position = self.ball_two_y_position + self.ball_two_y_change
        self.ball_two_image_label.place(x=self.ball_two_x_position, y=self.ball_two_y_position)
        
        self.after(100, self.tick)

    # the ball image
    def add_ball_one_image_label(self):
        self.ball_one_image_label = Label()
        self.ball_one_image_label.place(x=self.ball_one_x_position, y=self.ball_one_y_position)
        self.ball_one_image_label.configure(image=self.ball_one_image)

    def add_ball_two_image_label(self):
        self.ball_two_image_label = Label()
        self.ball_two_image_label.place(x=self.ball_two_x_position, y=self.ball_two_y_position)
        self.ball_two_image_label.configure(image=self.ball_two_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
