import threading
import tkinter
from tkinter import *
import socket
from PIL import ImageTk, Image
from tkinter import ttk, messagebox


class Winner(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('700x400')
        self.resizable(width=False, height=False)
        self.title('Winner Screen')

        self.create_gui()

    def create_gui(self):
        self.configure(bg='#00a8f3')  # -using color HEX
        # ----------------------------------------------------------------------------------------------
        self.placeStagelogo = "place stage.png"
        self.logoimg = Image.open(self.placeStagelogo)
        self.resizeble = self.logoimg.resize((300, 160), Image.Resampling.LANCZOS)
        self.placeStage = ImageTk.PhotoImage(self.resizeble)
        self.lbl_logoplaceStage = Label(self, image=self.placeStage, bg='#00a8f3')
        self.lbl_logoplaceStage.place(x=210, y=238)
        # ----------------------------------------------------------------------------------------------


