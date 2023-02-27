import threading
import tkinter
from tkinter import *
import socket


class Winner(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('500x300')
        self.resizable(width=False, height=False)
        self.title('Winner Screen')