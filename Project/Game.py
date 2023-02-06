import threading
import time
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
#from users import  *
from PIL import ImageTk, Image
from UserDB import *


#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
class Game(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('1200x600')
        self.resizable(width=False, height=False)
        self.title('Game Screen')
        self.userDb = UserDB()

        self.create_gui()

    def create_gui(self):
        self.configure(bg='#ffb838')  # -using color HEX
        # ----------------------------------------------------------------------------------------------
        self.ent_guess = Entry(self, font=50)
        self.ent_guess.place(x=430, y=450)
        # ----------------------------------------------------------------------------------------------
        self.btn_guess = Button(self, text='GUESS',command= self.Guess_img , font=30, background="#b7f061")
        self.btn_guess.place(x=500, y=500)


    def Guess_img(self):
        pass
