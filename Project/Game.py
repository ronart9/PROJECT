import threading
import time
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
#from users import  *
from PIL import ImageTk, Image
from UserDB import *
import random



#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
class Game(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('1105x600')
        self.resizable(width=False, height=False)
        self.title('Game Screen')
        self.userDb = UserDB()

        self.arrImg = [["tree", "../Project/images/tree.png"],
                       ["ghost", "../Project/images/ghost.png"] ,
                       ["car", "../Project/images/car.png"] ,
                       ["banana", "../Project/images/banana.png"],
                       ["beach", "../Project/images/beach.png"],
                       ["dog", "../Project/images/dog.png"],
                       ["python", "../Project/images/python.png"],
                       ["burger", "../Project/images/burger.png"]]

        self.create_gui()

    def create_gui(self):
        self.configure(bg='#ffb838')  # -using color HEX
        # ----------------------------------------------------------------------------------------------
        self.ent_guess = Entry(self, font=50)
        self.ent_guess.place(x=430, y=450)
        # ----------------------------------------------------------------------------------------------
        self.btn_guess = Button(self, text='GUESS',command= self.Guess_img , font=30, background="#b7f061")
        self.btn_guess.place(x=500, y=500)
        # ----------------------------------------------------------------------------------------------
        #self.UploadImg()
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


    def UploadImg(self):
        self.randomNum = self.random_num(len(self.arrImg) - 1)
        self.img_add = self.arrImg[self.randomNum][1]
        self.img_ad = Image.open(self.img_add)
        self.resized = self.img_ad.resize((500, 400), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.resized)
        self.lbl_img = Label(self, image=self.img)
        self.lbl_img.place(x=300, y=30)


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

    def GameF(self):
        try:
            self.roundLBL = StringVar()
            toprounds = len(self.arrImg)
            self.roundLBL.set("1 / " + str(toprounds))
            self.lab_rounds = Label(self, textvariable=self.roundLBL, fg='#000000', bg='#ffb838',
                                    font=('Helvetica bold', 25))
            self.lab_rounds.place(x=70, y=500)
            for i in range(toprounds):
                self.ent_guess.delete(0, END)
                self.roundLBL.set(str(i+1) + " / " + str(toprounds))
                self.guessLBL.set("guess the word:")
                self.UploadImg()
                while self.guessLBL.get() != "correct":
                    self.update()
            self.guessLBL.set("YOU WON !!")
            self.ent_guess.delete(0, END)
            self.ent_guess.config(state="disabled")
            self.btn_guess.config(state="disabled")





        except:
            print("error")

