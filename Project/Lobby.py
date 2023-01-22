import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
#from users import  *
from PIL import ImageTk, Image

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
        self.title('add user/register')
        #self.img = Image.open('what.jpg')
        #self.resize = self.img.resize((600, 450), Image.Resampling.LANCZOS)
        #self.bg = ImageTk.PhotoImage(self.resize)
        #self.imgLabel = Label(self, image=self.bg)
        #self.imgLabel.pack(expand=YES)
        #self.userdb= User()

        self.create_gui()


    def create_gui(self):
        self.configure(bg='#909090')  # -using color HEX
        # ----------------------------------------------------------------------------------------------
        self.btn_close = Button(self, text='Close', command=self.close, font=('Helvetica bold', 12),
                                background="#ea1111")
        self.btn_close.place(x=420, y=20)
        # ----------------------------------------------------------------------------------------------
        self.Conn_Pl = StringVar()
        self.Conn_Pl.set("Waiting for Player 2...")
        self.lab_plz_login = Label(self, textvariable=self.Conn_Pl, fg='#183652', bg = '#7190ab',font=('Helvetica bold', 16))
        self.lab_plz_login.place(x=150, y=260)




    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.SLobby, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def SLobby(self):
        pass

    def close(self):
        self.parent.deiconify() #show parent
        self.destroy()# close and destroy this screen