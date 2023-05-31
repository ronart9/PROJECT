import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
#from users import  *
from PIL import ImageTk, Image

class History(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('700x400')
        self.resizable(width=False, height=False)
        self.title('history')

        self.create_gui()

    def create_gui(self):
        self.configure(bg='#6ea7db')  # -using color HEX
        # ----------------------------------------------------------------------------------------------
        self.btn_close = Button(self, text='Close', command=self.close, font=('Helvetica bold', 12),
                                background="#ea1111")
        self.btn_close.place(x=560, y=50)
        # ----------------------------------------------------------------------------------------------
        self.table = ttk.Treeview(self, columns=("GameId", "Player1", "Player2", "Winner"), show="headings", height=7)
        self.table.column("GameId", anchor=CENTER, width=100)
        self.table.column("Player1", anchor=CENTER, width=100)
        self.table.column("Player2", anchor=CENTER, width=100)
        self.table.column("Winner", anchor=CENTER, width=100)
        self.table.heading("GameId", text="Game ID")
        self.table.heading("Player1", text="Player 1")
        self.table.heading("Player2", text="Player 2")
        self.table.heading("Winner", text="Winner")
        self.table.place(x=130, y=120)
        self.History_Menu()


    def History_Menu(self):
        try:
            self.parent.send_data("GetHistory", self.parent.client_socket)
            data = self.parent.recv_data(self.parent.client_socket, "pickle")
            print(data)
            if not data:
                print("No data ")
                return
            for item in data:
                line = item.split()
                game_id = line[0]
                player1 = line[1]
                player2 = line[2]
                winner = line[3]
                self.table.insert("", "end", values=(game_id, player1, player2, winner), tags=("data",))
        except:
            print("fail - history tbl")


    def close(self):
        self.parent.deiconify() #show parent
        self.destroy()# close and destroy this screen