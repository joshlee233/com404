from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        self.title("SongMaker")

        self.__add_heading_label()
        self.__add_subheading_one_label()
        self.__add_main_frame()
        self.__add_lyric_entry()
        self.__add_addlyric_button()
        self.__add_subheading_two_label()
        self.__add_lyric_box()
        

    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)

        self.heading_label.configure(text="Song Maker", font="Arial 24", fg="#000")

    def __add_subheading_one_label(self):
        self.subheading_one_label = Label()
        self.subheading_one_label.grid(row=1, column=0, sticky=W)

        self.subheading_one_label.configure(text="Lyric to add:", font="Arial 16", fg="#000")

    def __add_main_frame(self):
        self.main_frame = Frame()
        self.main_frame.grid(row=2, column=0)
    
    def __add_lyric_entry(self):
        self.lyric_entry = Entry(self.main_frame)
        self.lyric_entry.pack(side=LEFT)
        

    def __add_addlyric_button(self):
        self.addlyric_button = Button(self.main_frame)
        self.addlyric_button.pack(side=RIGHT)
        self.addlyric_button.configure(text="Add", font="Arial 16", padx=20)

        self.addlyric_button.bind("<ButtonRelease-1>", self.__add_button_clicked)

    def __add_subheading_two_label(self):
        self.subheading_two_label = Label()
        self.subheading_two_label.grid(row=3, column=0, sticky=W)
        self.subheading_two_label.configure(text="Lyrics:", font="Arial 16", fg="#000")

    def __add_lyric_box(self):
        self.lyric_box = Listbox()
        self.lyric_box.grid(row=4, column=0, sticky=N+E+S+W)

    def __add_button_clicked(self, event):
         added_lyrics= self.lyric_entry.get()
         self.lyric_box.insert(END, added_lyrics)
        
       
        
