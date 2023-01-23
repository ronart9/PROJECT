import threading
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
class Lobby(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('500x300')
        self.resizable(width=False, height=False)
        self.title('Waiting Lobby')
        #self.img = Image.open('what.jpg')
        #self.resize = self.img.resize((600, 450), Image.Resampling.LANCZOS)
        #self.bg = ImageTk.PhotoImage(self.resize)
        #self.imgLabel = Label(self, image=self.bg)
        #self.imgLabel.pack(expand=YES)
        #self.userdb= User()
        self.userDb = UserDB()

        self.create_gui()


    def create_gui(self):
        self.configure(bg='#909090')  # -using color HEX
        # ----------------------------------------------------------------------------------------------
        self.btn_close = Button(self, text='Leave', command=self.close, font=('Helvetica bold', 12),
                                background="#ea1111")
        self.btn_close.place(x=420, y=20)
        # ----------------------------------------------------------------------------------------------
        self.Conn_Pl = StringVar()
        self.Conn_Pl.set("Waiting for Player 2...")
        self.lab_plz_login = Label(self, textvariable=self.Conn_Pl, fg='#183652', bg = '#7190ab',font=('Helvetica bold', 16))
        self.lab_plz_login.place(x=150, y=260)
        # ----------------------------------------------------------------------------------------------
        self.logoLb = "LobbyFrameP1.png"
        self.logoimgLb = Image.open(self.logoLb)
        self.resizeble = self.logoimgLb.resize((220, 160), Image.Resampling.LANCZOS)
        self.LobbyImg = ImageTk.PhotoImage(self.resizeble)
        self.lbl_LobbyImg = Label(self, image=self.LobbyImg, bg='#909090')
        self.lbl_LobbyImg.place(x=25, y=60)
        # ----------------------------------------------------------------------------------------------
        self.data= self.parent.Lobby_data()
        self.lab_P1 = Label(self, text= self.data,
                            font=('Helvetica bold', 15), bg='#747474')
        self.lab_P1.place(x=60, y=120)
        # ----------------------------------------------------------------------------------------------
        self.Name_P2 = self.parent.client_socket.recv(1024).decode('utf-8')
        self.lbl_NameP2 = Label(self, text= self.Name_P2, font=('Helvetica bold', 15), bg='#747474')
        self.lbl_NameP2.place(x= 160, y = 120)




    def SLobby(self):
        pass

    def close(self):
        self.parent.deiconify() #show parent
        self.destroy()# close and destroy this screen