import threading
import time
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
#from users import  *
from PIL import ImageTk, Image
from UserDB import *
import random
from Winner import Winner



#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
class Game(tkinter.Toplevel):
    def __init__(self, parent): #1
        super().__init__(parent)
        self.parent = parent
        self.geometry('1105x600')
        self.resizable(width=False, height=False)
        self.title('Game Screen')
        self.userDb = UserDB()
        self.flag = False
        self.RunningGame = True
        self.RunningRecv = True
        self.god = parent.parent
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.arrImg = [["tree", "../Project/images/tree.png"],
                       ["ghost", "../Project/images/ghost.png"] ,
                       ["car", "../Project/images/car.png"] ,
                       ["banana", "../Project/images/banana.png"],
                       ["beach", "../Project/images/beach.png"],
                       ["dog", "../Project/images/dog.png"],
                       ["python", "../Project/images/python.png"],
                       ["burger", "../Project/images/burger.png"],
                       ["robot", "../Project/images/robot.PNG"],
                       ["panda", "../Project/images/panda.PNG"],
                       ["city", "../Project/images/city.jpg"],
                       ["skull", "../Project/images/skull.png"],
                       ["racoon", "../Project/images/racoon.png"],
                       ["crow", "../Project/images/crow.PNG"],
                       ["ship", "../Project/images/ship.jpg"],
                       ["pasta", "../Project/images/pasta.png"]]
        self.arr2 = []

        self.create_gui()

    def create_gui(self): #2
        self.configure(bg='#ffb838')  # -using color HEX
        # ----------------------------------------------------------------------------------------------
        self.bg_P2stats = Canvas(self, width=200, height=290, bg='#ee890c', highlightthickness=0)
        self.bg_P2stats.place(x=50, y=100)
        # ----------------------------------------------------------------------------------------------
        self.lab_stats = Label(self, text='STATS', font=('Helvetica bold', 25), bg='#ee890c')
        self.lab_stats.place(x=75, y=115)
        # ----------------------------------------------------------------------------------------------
        self.lab_round1 = Label(self, text='rounds', font=('Helvetica bold', 15), bg='#ee890c')
        self.lab_round1.place(x=170, y=210)
        # ----------------------------------------------------------------------------------------------
        self.lab_line = Label(self, text='-------------------------', font=('Helvetica bold', 15), bg='#ee890c')
        self.lab_line.place(x=60, y=240)
        # ----------------------------------------------------------------------------------------------
        self.lab_round2 = Label(self, text='rounds', font=('Helvetica bold', 15), bg='#ee890c')
        self.lab_round2.place(x=170, y=325)
        # ----------------------------------------------------------------------------------------------
        self.ent_guess = Entry(self, font=50)
        self.ent_guess.place(x=430, y=450)
        # ----------------------------------------------------------------------------------------------
        self.btn_guess = Button(self, text='GUESS',command= self.Guess_img , font=30, background="#b7f061")
        self.bind("<Return>", lambda event: self.btn_guess.invoke())
        self.btn_guess.place(x=500, y=500)
        # ----------------------------------------------------------------------------------------------
        self.guessLBL = StringVar()
        self.guessLBL.set("guess the word:")
        self.lab_wtg = Label(self, textvariable=self.guessLBL, fg='#000000', bg='#daae29', font=('Helvetica bold', 16))
        self.lab_wtg.place(x=900, y=500)
        # ----------------------------------------------------------------------------------------------
        self.lab_capitals = Label(self, text= "* make sure to NOT use capital letters *", fg='#c22620', bg='#ffb838', font=('Helvetica bold', 9))
        self.lab_capitals.place(x=430, y=480)
        # ----------------------------------------------------------------------------------------------
        self.handle_thread_gamef()


    #def button_pressed(self):
        #self.btn_guess.invoke()

    def UploadImg(self):
        #self.random_nums = []
        #not_same = True
        self.randomNum = self.random_num(len(self.arrImg) - 1)
        #while not_same == True:
            #if (self.randomNum in self.random_nums):
                #self.randomNum = self.random_num(len(self.arrImg) - 1)
            #else:
                #not_same = False
        #self.random_nums.append(self.randomNum)
        self.img_add = self.arrImg[self.randomNum][1]
        self.img_ad = Image.open(self.img_add)
        self.resized = self.img_ad.resize((500, 400), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.resized)
        #self.arr2.append(self.arrImg[self.randomNum])
        self.lbl_img = Label(self, image=self.img)
        self.lbl_img.place(x=300, y=30)
        #self.arrImg.remove(self.arrImg[self.randomNum])



    def random_num(self, num):
        return random.randint(0, num)



    def Guess_img(self):
        try:
            if (self.ent_guess.get() == self.arrImg[self.randomNum][0]):
                self.guessLBL.set("correct")
                #self.lab_wtg.config(fg="23e804")
            else:
                self.guessLBL.set("false")
                #self.lab_wtg.config(fg= "red")
                self.ent_guess.delete(0, END)
        except:
            self.guessLBL.set("error")

    def handle_thread_gamef(self):
        client_handler = threading.Thread(target=self.GameF, args=())
        client_handler.daemon = True
        client_handler.start()

    def handle_thread_rounds(self):
        self.client_round = threading.Thread(target=self.recv_rounds, args=())
        self.client_round.daemon = True
        self.client_round.start()

    def handle_thread_WinSc(self):
        self.client_round = threading.Thread(target=self.recv_WinSc, args=())
        self.client_round.daemon = True
        self.client_round.start()

    def recv_rounds(self):
        try:
            while self.RunningRecv:
                if self.flag:
                    return
                #data_RC12 = self.parent.parent.client_socket.recv(1024).decode()
                data_RC12 = self.god.recv_data(self.god.client_socket)
                arr_RC12 = data_RC12.split(",")
                print(arr_RC12)
                if arr_RC12 and arr_RC12[1] == 'CloseWindowGame':
                    self.RunningRecv = False
                    self.OpenWinScreen()
                elif arr_RC12 and arr_RC12[1] == "DataDisP2":
                    print("recv here")
                    self.LabelExit = Label(self, text=f"{self.nameP2} has disconnected.", fg="red", bg='#ffb838', font=('Helvetica bold', 16))
                    self.LabelExit.place(x=415, y=550)
                    time.sleep(5)
                    self.god.destroy()
                elif arr_RC12[1] == 'This_Round':
                    self.roundLBL2.set(str(arr_RC12[0]) + " / 10")
        except ConnectionRefusedError:
            # Server connection failed
            messagebox.showerror("Connection Error", "Failed to connect to the server.")
            self.destroy()
        except ConnectionResetError as e:
            # Server connection forcibly closed
            print("GG-Connection reset error:", str(e))
            # Perform any necessary cleanup or reset the application state
            print("error conn server-client - recvGame")
            self.error_label = Label(self, text="The server has disconnected.", fg="red", bg='#ffb838', font=('Helvetica bold', 16))
            self.error_label.place(x=405, y=550)
            self.btn_guess.configure(state= "disabled")
            time.sleep(5)
            self.god.client_socket.close()
            # You can provide an option for the user to reconnect or exit the application
            self.god.destroy()
        except:
            print("something went wrong in recv data")

    def recv_WinSc(self):
        while True:
            #data_WS = self.parent.parent.client_socket.recv(1024).decode()
            data_WS = self.god.recv_data(self.god.client_socket)
            arr_WS = data_WS.split(",")
            print(arr_WS)
            print("recvWinSC")
            if arr_WS[1] == "CloseWindowGame":
                self.OpenWinScreen()

    def on_closing(self):
        self.Arr = ["exitOnGame", self.username]
        self.ArrData = ",".join(self.Arr)
        self.god.send_data(self.ArrData, self.god.client_socket)
        self.god.destroy()


    def GameF(self):
        try:
            self.username = self.parent.parent.username
            self.U2 = ["UserNameP2", str(self.username)]
            self.data_U2 = ",".join(self.U2)
            #self.parent.parent.client_socket.send(self.data_U2.encode())
            self.god.send_data(self.data_U2, self.god.client_socket)
            #self.data_nameP2 = self.parent.parent.client_socket.recv(1024).decode()
            self.data_nameP2 = self.god.recv_data(self.god.client_socket)
            self.arr_nameP2 = self.data_nameP2.split(",")
            self.nameP2 = self.arr_nameP2[0]
            print("hello im P1 "+ str(self.username))
            print("hello im P2: "+ str(self.nameP2))
            self.lab_nameP1 = Label(self, text=str(self.username), font=('Helvetica bold', 25),
                                    bg='#ee890c', fg = '#4c9e18')
            self.lab_nameP1.place(x=80, y=160)
            self.lab_nameP2 = Label(self, text=str(self.nameP2), font=('Helvetica bold', 25),
                                    bg='#ee890c', fg = '#e80000')
            self.lab_nameP2.place(x=80, y=275)

            self.roundLBL = StringVar()
            self.roundLBL2 = StringVar()
            toprounds = 10
            self.roundLBL.set("1 / " + str(toprounds))
            self.roundLBL2.set("1 / " + str(toprounds))
            self.handle_thread_rounds()
            self.lab_rounds = Label(self, textvariable=self.roundLBL, fg='#000000', bg='#ee890c',
                                    font=('Helvetica bold', 25))
            self.lab2_rounds = Label(self, textvariable=self.roundLBL2, fg='#000000', bg='#ee890c',
                                    font=('Helvetica bold', 25))
            self.lab_rounds.place(x=60, y=205)
            self.lab2_rounds.place(x=60, y=320)
            self.rounds1 = 0
            self.rounds2 = 0
            while self.RunningGame:
                for i in range(toprounds):
                    #self.handle_thread_WinSc()
                    self.rounds1 += 1
                    self.arr_rounds = ["Rounds", str(self.username), str(self.rounds1)]
                    data_rounds = ",".join(self.arr_rounds)
                    #self.parent.parent.client_socket.send(data_rounds.encode())
                    self.god.send_data(data_rounds , self.god.client_socket)

                    self.ent_guess.delete(0, END)
                    self.roundLBL.set(str(i+1) + " / " + str(toprounds))
                    self.guessLBL.set("guess the word:")
                    self.UploadImg()
                    while self.guessLBL.get() != "correct":
                        self.update()
                self.flag = True
                self.guessLBL.set("YOU WON !!")
                self.ent_guess.delete(0, END)
                self.ent_guess.config(state="disabled")
                self.btn_guess.config(state="disabled")
                username = self.parent.username
                arr = ["WinScreen", username]
                data = ",".join(arr)

                #self.parent.parent.client_socket.send(data.encode())
                self.god.send_data(data, self.god.client_socket)
                #self.handle_thread_WinSc()

                #for n in range(len(self.arr2)):
                    #self.arrImg.append(self.arr2[n])
                    #self.arr2.remove(self.arr2[n])
        except ConnectionRefusedError:
            # Server connection failed
            messagebox.showerror("Connection Error", "Failed to connect to the server.")
            self.destroy()
        except ConnectionResetError as e:
            # Server connection forcibly closed
            print("G-Connection reset error:", str(e))
            self.god.client_socket.close()
            # Perform any necessary cleanup or reset the application state
            # You can provide an option for the user to reconnect or exit the application
            self.god.destroy()
        except:
            print("error - GameF")


    def OpenWinScreen(self):
        window = Winner(self)
        window.grab_set()
        self.withdraw()