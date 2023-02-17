import threading
import time
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
#from users import  *
from PIL import ImageTk, Image
from UserDB import *
from Game import Game


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
        self.userDb = UserDB()

        self.create_gui()

        self.waiting_list = ["me"]



    def create_gui(self):
        self.configure(bg='#909090')  # -using color HEX
        # ----------------------------------------------------------------------------------------------
        self.btn_close = Button(self, text='Leave', command=self.close, font=('Helvetica bold', 12),
                                background="#ea1111")
        self.btn_close.place(x=420, y=20)
        # ----------------------------------------------------------------------------------------------
        self.Conn_Pl = StringVar()
        self.Conn_Pl.set("Waiting for Player 2..." )
        self.lab_wtg = Label(self, textvariable=self.Conn_Pl, fg='#1ef800', bg = '#909090',font=('Helvetica bold', 16))
        self.lab_wtg.place(x=35, y=240)
        # ----------------------------------------------------------------------------------------------
        self.logoLb = "LobbyFrameP1.png"
        self.logoimgLb = Image.open(self.logoLb)
        self.resizeble = self.logoimgLb.resize((220, 160), Image.Resampling.LANCZOS)
        self.LobbyImg = ImageTk.PhotoImage(self.resizeble)
        self.lbl_LobbyImg = Label(self, image=self.LobbyImg, bg='#909090')
        self.lbl_LobbyImg.place(x=25, y=60)
        # ----------------------------------------------------------------------------------------------
        self.logoTi = "TimerSetLogo.png"
        self.logoimgTi = Image.open(self.logoTi)
        self.resizebleTi = self.logoimgTi.resize((220, 160), Image.Resampling.LANCZOS)
        self.LobbyImgTi = ImageTk.PhotoImage(self.resizebleTi)
        self.lbl_LobbyImg = Label(self, image=self.LobbyImgTi, bg='#909090')
        self.lbl_LobbyImg.place(x=260, y=70)
        # ----------------------------------------------------------------------------------------------
        self.Timer = StringVar()
        self.Timer.set("")
        self.lab_timer = Label(self, textvariable=self.Timer, fg='#ffffff', bg='#141850', font=('Helvetica bold', 16))
        self.lab_timer.place(x=353, y=142)
        # ----------------------------------------------------------------------------------------------
        self.logo = "img_2.png"
        self.logoimg = Image.open(self.logo)
        self.resizeble = self.logoimg.resize((100, 25), Image.Resampling.LANCZOS)
        self.paint = ImageTk.PhotoImage(self.resizeble)
        self.lbl_LobbyTXT = Label(self, bg='#909090' , image=self.paint)
        self.lbl_LobbyTXT.place(x=80, y=35)
        # ----------------------------------------------------------------------------------------------
        self.list = Listbox(self , height = 6, bg = "black", fg= "green", )
        email = self.parent.ent_email.get()
        password = self.parent.ent_password.get()
        self.username = self.parent.username
        #username = self.userDb.return_user_by_email(email, password)
        self.list.insert(1, self.username)
        self.list.place(x= 65, y= 92)

        self.handle_waiting_for_player()
        self.handle_waiting_for_message()



    def SGame(self):
        window = Game(self)
        window.grab_set()
        self.withdraw()


    def handle_waiting_for_player(self):
        self.Client_handler = threading.Thread(target=self.waiting_for_player, args=())
        self.Client_handler.daemon = True
        self.Client_handler.start()

    def handle_waiting_for_message(self):
        self.Client_handler = threading.Thread(target=self.waiting_for_message, args=())
        self.Client_handler.daemon = True
        self.Client_handler.start()

    def waiting_for_player(self):
        #email = self.parent.ent_email.get()
        #password = self.parent.ent_password.get()
        username = self.parent.username
        arr = ["JoinLobby", username]
        data = ",".join(arr)
        self.parent.client_socket.send(data.encode())
        data = self.parent.client_socket.recv(1024).decode()
        arr = data.split(",")
        print(arr)
        self.num = 2
        if(arr[1] == "wait"):
            data = self.parent.client_socket.recv(1024).decode()
            data = data.split(",")
            #self.num1set = 2
            self.list.insert(2, data[0]+ f" [player {self.num}]")
            self.Animation_Ent_Lobby()
        elif(arr[1] == "start"):
            print(arr[0], " join us ")
            #self.num2set= 1
            self.list.insert(2, arr[0]+ f" [player {self.num}]")
            self.Animation_Ent_Lobby()

    def waiting_for_message(self):
        data = self.parent.client_socket.recv(1024).decode()
        if data == "playerleave":
            self.Conn_Pl.set("Pleyer left...")
            time.sleep(1)
            self.Conn_Pl.set("Waiting for Player 2...")
            self.handle_waiting_for_player()

    def Animation_Ent_Lobby(self):
        self.Conn_Pl.set("Pleyer 2 connected")
        time.sleep(1)
        self.Conn_Pl.set("Pleyer 2 connected .")
        time.sleep(1)
        self.Conn_Pl.set("Pleyer 2 connected ..")
        time.sleep(1)
        self.Conn_Pl.set("Pleyer 2 connected ...")
        time.sleep(1)
        self.Conn_Pl.set("")
        time.sleep(0.3)
        self.Conn_Pl.set("S")
        time.sleep(0.3)
        self.Conn_Pl.set("sT")
        time.sleep(0.3)
        self.Conn_Pl.set("stA")
        time.sleep(0.3)
        self.Conn_Pl.set("staR")
        time.sleep(0.3)
        self.Conn_Pl.set("starT")
        time.sleep(0.3)
        self.Conn_Pl.set("startinG")
        time.sleep(0.3)
        self.Conn_Pl.set("starting G")
        time.sleep(0.3)
        self.Conn_Pl.set("starting gA")
        time.sleep(0.3)
        self.Conn_Pl.set("starting gaM")
        time.sleep(0.3)
        self.Conn_Pl.set("starting gamE")
        time.sleep(0.3)
        self.Conn_Pl.set("starting game I")
        time.sleep(0.3)
        self.Conn_Pl.set("starting game iN")
        time.sleep(0.3)
        self.Conn_Pl.set("starting game in -")
        time.sleep(0.3)
        self.Conn_Pl.set("starting game in ->")
        time.sleep(1)
        self.Timer.set("5")
        time.sleep(1)
        self.Timer.set("4")
        time.sleep(1)
        self.Timer.set("3")
        time.sleep(1)
        self.Timer.set("2")
        time.sleep(1)
        self.Timer.set("1")
        time.sleep(1)
        self.Timer.set("")
        time.sleep(1)
        self.SGame()

    def remove_player(self, player):
        index = self.list.get(0, END).index(player)
        self.list.delete(index)

    def close(self):
        #self.list.delete(0, END)
        #self.remove_player(self.parent.username)
        message = ["LeaveLobby", self.parent.username]
        data = ",".join(message)
        self.parent.client_socket.send(data.encode())
        #message = self.parent.client_socket.recv(1024).decode()
        self.parent.deiconify() #show parent
        self.destroy()# close and destroy this screen