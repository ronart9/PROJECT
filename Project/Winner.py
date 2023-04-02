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

        # ----------------------------------------------------------------------------------------------
        self.LoserLBL = StringVar()
        self.LoserLBL.set("")

        # ----------------------------------------------------------------------------------------------
        self.btn_close = Button(self, text='Close', command=self.close, font=('Helvetica bold', 12),
                                background="#ea1111")
        self.btn_close.place(x=600, y=50)
        # ----------------------------------------------------------------------------------------------
        self.handle_thread_GetWL()


    def handle_thread_GetWL(self):
        client_handler = threading.Thread(target=self.Get_Win_lose, args=())
        client_handler.daemon = True
        client_handler.start()

    def Get_Win_lose(self):
        try:
            self.username = self.parent.parent.parent.username
            self.parent.parent.parent.client_socket.send("Winner_Loser".encode())
            self.data_WL = self.parent.parent.parent.client_socket.recv(1024).decode()
            self.arr_WL = self.data_WL.split(",")
            print("WWWWWWWWWWWWWWW")
            print(self.arr_WL)
            if self.arr_WL[0] == self.username:
                self.Won = "img_6.png"
                self.Wonimg = Image.open(self.Won)
                self.resizebleW = self.Wonimg.resize((320, 150), Image.Resampling.LANCZOS)
                self.WonL = ImageTk.PhotoImage(self.resizebleW)
                self.lbl_logoWon = Label(self, image=self.WonL, bg='#00a8f3')
                self.lbl_logoWon.place(x=195, y=30)
                # ----------------------------------
                self.lab_Winner = Label(self, textvariable=self.WinnerLBL, fg='#4de100', bg='#00a8f3',
                                        font=('Comic Sans MS', 16))
                self.lab_Winner.place(x=240, y=205)
                # ----------------------------------
                self.lab_Loser = Label(self, textvariable=self.LoserLBL, fg='#ee0000', bg='#00a8f3',
                                       font=('Comic Sans MS', 16))
                self.lab_Loser.place(x=400, y=240)
            elif self.arr_WL[1] == self.username:
                self.Lost = "img_7.png"
                self.Lostimg = Image.open(self.Lost)
                self.resizebleL = self.Lostimg.resize((320, 150), Image.Resampling.LANCZOS)
                self.LostL = ImageTk.PhotoImage(self.resizebleL)
                self.lbl_logoLost = Label(self, image=self.LostL, bg='#00a8f3')
                self.lbl_logoLost.place(x=195, y=30)
                # ----------------------------------
                self.lab_Winner = Label(self, textvariable=self.WinnerLBL, fg='#ee0000', bg='#00a8f3',
                                        font=('Comic Sans MS', 16))
                self.lab_Winner.place(x=240, y=205)
                # ----------------------------------
                self.lab_Loser = Label(self, textvariable=self.LoserLBL, fg='#4de100', bg='#00a8f3',
                                       font=('Comic Sans MS', 16))
                self.lab_Loser.place(x=400, y=240)


            self.WinnerLBL.set(str(self.arr_WL[0]))
            self.LoserLBL.set(str(self.arr_WL[1]))


        except:
            print("error")


    def close(self):
        self.parent.parent.parent.deiconify() #show parent
        self.destroy()# close and destroy this screen


