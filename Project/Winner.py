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
        self.WinnerLBL = StringVar()
        self.WinnerLBL.set("")
        self.lab_Winner = Label(self, textvariable=self.WinnerLBL, fg='#000000', bg='#00a8f3',
                                font=('Helvetica bold', 16))
        self.lab_Winner.place(x=230, y=200)
        # ----------------------------------------------------------------------------------------------
        self.LoserLBL = StringVar()
        self.LoserLBL.set("")
        self.lab_Loser = Label(self, textvariable=self.LoserLBL, fg='#000000', bg='#00a8f3',
                                font=('Helvetica bold', 16))
        self.lab_Loser.place(x=410, y=250)
        # ----------------------------------------------------------------------------------------------
        self.handle_thread_GetWL()


    def handle_thread_GetWL(self):
        client_handler = threading.Thread(target=self.Get_Win_lose, args=())
        client_handler.daemon = True
        client_handler.start()

    def Get_Win_lose(self):
        try:
            self.parent.parent.parent.client_socket.send("Winner_Loser".encode())
            self.data_WL = self.parent.parent.parent.client_socket.recv(1024).decode()
            self.arr_WL = self.data_WL.split(",")
            print("WWWWWWWWWWWWWWW")
            print(self.arr_WL)
            self.WinnerLBL.set(str(self.arr_WL[0]))
            self.LoserLBL.set(str(self.arr_WL[1]))


        except:
            print("error")


