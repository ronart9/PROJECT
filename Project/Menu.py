import threading
import tkinter
from tkinter import *
from Register import Register
# from login import Login
import socket
# from users import User
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from Lobby import Lobby
import time
from History import *
SIZE = 8
import pickle
#from cryptography.hazmat.primitives.asymmetric import padding
#from cryptography.hazmat.primitives import hashes
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

from tkinter import ttk
import tkinter as tk


# from tkfontawesome import icon_to_image

# https://www.pythontutorial.net/tkinter/tkinter-toplevel/
# toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
# it is just a variable to hold the top level, 'window'
# should be whatever variable holds your main window
# toplevel.title = 'Top Level'

class Menu_Screen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1200x600')
        self.resizable(width=False, height=False)
        self.title('Main Window')
        self.username = ""
        self.wm_iconbitmap('sketchbook.ico')
        self.format = 'utf-8'
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.create_gui()

    def create_gui(self):
        self.configure(bg='#856ff8')  # -using color HEX
        # ----------------------------------------------------------------------------------------------
        #self.icon = PhotoImage("img_5.png")
        #self.iconphoto(False, self.icon)
        # ----------------------------------------------------------------------------------------------
        self.bg_Log = Canvas(self, width=350, height=500, bg= '#856ff8', highlightthickness= 0)
        self.bg_Log.create_rectangle(10, 10, 320, 480, outline="#5b3cbd", width= 5 ,fill= "#5b3cbd")
        self.bg_Log.place(x= 50, y= 50)
        # ----------------------------------------------------------------------------------------------
        self.flag = False
        # ----------------------------------------------------------------------------------------------
        #self.emailvar = StringVar()
        self.lab_email = Label(self, text='Enter Email: ', font=('Helvetica bold', 15), bg='#5b3cbd')
        self.lab_email.place(x=100, y=120)
        self.ent_email = Entry(self, font=40)
        self.ent_email.place(x=100, y=165)
        # ----------------------------------------------------------------------------------------------
        self.lab_password = Label(self, text='Enter Password: ', font=('Helvetica bold', 15), bg='#5b3cbd')
        self.lab_password.place(x=100, y=235)
        self.ent_password = Entry(self, show="*", font=40)
        self.ent_password.place(x=100, y=280)
        # ----------------------------------------------------------------------------------------------
        self.img3_adress = "img_1.png"
        self.imgeye = Image.open(self.img3_adress)
        self.resized3 = self.imgeye.resize((25, 25), Image.Resampling.LANCZOS)
        self.eye = ImageTk.PhotoImage(self.resized3)
        # ----------------------------------------------------------------------------------------------

        self.img2_adress = "img.png"
        self.imgeyeclose = Image.open(self.img2_adress)
        self.resized2 = self.imgeyeclose.resize((25, 25), Image.Resampling.LANCZOS)
        self.eyeclose = ImageTk.PhotoImage(self.resized2)
        self.btn_eye_closed = Button(self, text='Clear', command=self.HideShowEye, font=('Helvetica bold', 12),
                                image=self.eyeclose)  # background= "#f86060"
        self.btn_eye_closed.place(x=330, y=280)
        # ----------------------------------------------------------------------------------------------
        self.btn_login = Button(self, text='Login', command=self.log_in, font=30, background="#b7f061")
        self.btn_login.place(x=100, y=350)
        # ----------------------------------------------------------------------------------------------
        self.btn_register = Button(self, text='Register', command=self.open_register, font=30, background="#ffd966")
        self.btn_register.place(x=100, y=420)
        # ----------------------------------------------------------------------------------------------
        self.img_adress ="garbage.png"
        self.imggarbage = Image.open(self.img_adress)
        self.resized = self.imggarbage.resize((35, 35), Image.Resampling.LANCZOS)
        self.garbage = ImageTk.PhotoImage(self.resized)
        self.btn_clear = Button(self, text='Clear', command=self.clear_text, font=('Helvetica bold', 12),
                                image=self.garbage)  # background= "#f86060"
        self.btn_clear.place(x=200, y=350)
        # ----------------------------------------------------------------------------------------------
        self.logo = "paint logo.png"
        self.logoimg = Image.open(self.logo)
        self.resizeble = self.logoimg.resize((500, 225), Image.Resampling.LANCZOS)
        self.paint = ImageTk.PhotoImage(self.resizeble)
        self.lbl_logopaint= Label(self, image = self.paint , bg='#856ff8')
        self.lbl_logopaint.place(x= 650, y= 10)
        # ----------------------------------------------------------------------------------------------
        self.logoLogin = "img_3.png"
        self.logoLoginimg = Image.open(self.logoLogin)
        self.resizebleLogin = self.logoLoginimg.resize((170, 30), Image.Resampling.LANCZOS)
        self.paintLogin = ImageTk.PhotoImage(self.resizebleLogin)
        self.lbl_logoLogin = Label(self, image=self.paintLogin, bg='#856ff8')
        self.lbl_logoLogin.place(x=120, y=20)
        # ----------------------------------------------------------------------------------------------
        self.plz = StringVar()
        self.plz.set("Please Login...")
        self.lab_plz_login = Label(self, textvariable=self.plz, bg='#856ff8' ,font=('Helvetica bold', 16))
        self.lab_plz_login.place(x=700, y=112)
        # ----------------------------------------------------------------------------------------------
        self.btn_ref = Button(self, text='refresh', command=self.refresh, font=20, background="#856ff8")
        # ----------------------------------------------------------------------------------------------
        self.btn_Ohis = Button(self, text='History', command=self.Open_history, font=30, background="#856ff8")
        self.btn_Ohis.place(x=850, y=500)
        # ----------------------------------------------------------------------------------------------
        self.handle_thread_socket()




    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()

    def handle_thread_wins(self):
        client_handler = threading.Thread(target=self.recv_wins, args=())
        client_handler.daemon = True
        client_handler.start()

    def create_socket(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(('127.0.0.1', 1827))
            self.dataPuKey = self.recv_data(self.client_socket)
            print("data " + self.dataPuKey)
            print("hi", self.client_socket)
        except:
            print("there is no server connaction")
            self.count_down()
            self.close()

    def log_in(self):
        try:
            email = self.ent_email.get()
            password = self.ent_password.get()
            arr = ["login", email, password]
            insert = ",".join(arr)
            print(insert)
            #self.client_socket.send(insert.encode())
            self.send_data(insert, self.client_socket, "zofen")
            #self.username = self.client_socket.recv(1024).decode()
            self.username = self.recv_data(self.client_socket)
            #data = self.client_socket.recv(1024).decode()
            data = self.recv_data(self.client_socket)
            d = str(data)
            print(d)
            if d[0] == 'W':
                self.plz.set(data)
                #print(data)
                self.logoJoin = "img_4.png"
                self.logoJoinimg = Image.open(self.logoJoin)
                self.resizebleJoin = self.logoJoinimg.resize((300, 100), Image.Resampling.LANCZOS)
                self.paintJoin = ImageTk.PhotoImage(self.resizebleJoin)
                self.Jlobby = Button(self, image= self.paintJoin,command = self.Open_Lobby, background="#2BB807")
                self.Jlobby.place(x=700, y=260)
                #self.clear_text()
                self.btn_login.place_forget()
                self.btn_logout = Button(self, text= "Logout", command= self.Log_out ,font=30, background= "#c7594b")
                self.btn_logout.place(x= 100, y= 350)
                self.ent_email.config(state= "disabled")
                self.ent_password.config(state="disabled")
                self.winsLBL = StringVar()
                self.lab_wins = Label(self, textvariable=self.winsLBL, fg='#000000', bg='#856ff8',
                                      font=('Helvetica bold', 20))
                self.lab_wins.place(x=776, y=420)
                self.btn_ref.place(x=750, y=500)
                self.arr_wins = ["wins", self.username]
                self.arrW = ",".join(self.arr_wins)
                self.send_data(self.arrW, self.client_socket)
                data_wins = self.recv_data(self.client_socket)
                arr_wins = data_wins.split(",")
                print(arr_wins)
                if arr_wins[1] == 'GotWins':
                    print("6")
                    self.winsLBL.set(str(arr_wins[0]))
                #self.handle_thread_wins()
            elif d[0] == 'F':
                self.plz.set(data)
                self.Jlobby.place_forget()
                messagebox.showerror("error message", "Error")
                print(data)
        except:
            print("error in log in")
            return False

    def open_register(self):
        try:
            window = Register(self)
            window.grab_set()
            self.withdraw()
        except:
            print("error opening register screen")

    def Open_history(self):
        try:
            window = History(self)
            window.grab_set()
            self.withdraw()
        except:
            print("error opening history screen")

    def count_down(self):
        for i in range(5, 0, -1):
            print(i)
            time.sleep(1)

    def clear_text(self):
        try:
            self.ent_email.delete(0, END)
            self.ent_password.delete(0, END)
        except:
            print("error clearing text")

    def Log_out(self):
        try:
            self.plz.set("Please Login...")
            self.Jlobby.place_forget()
            self.btn_logout.place_forget()
            self.btn_login.place(x= 100, y= 350)
            self.ent_email.config(state="normal")
            self.btn_ref.place_forget()
            self.lab_wins.place_forget()
            self.ent_password.config(state="normal")
            self.clear_text()
        except:
            print("error logging out")

    def on_closing(self):
        if messagebox.askokcancel("Quit Game", "Do you want to quit?"):
            self.send_data("exit", self.client_socket)
            self.destroy()


    def HideShowEye(self):
        try:
            if self.ent_password.cget("show")== '':
                self.ent_password.config(show= '*')
                self.btn_eye_closed.config(image=self.eye)
            else:
                self.ent_password.config(show= '')
                self.btn_eye_closed.config(image=self.eyeclose)
        except:
            print("failed to Hide & Show eye")

            return False

    def Open_Lobby(self):
        try:
            window = Lobby(self)
            window.grab_set()
            self.withdraw()
        except:
            print("error opening Lobby")




    def refresh(self):
        try:
            self.arr_wins = ["wins", self.username]
            self.arrW= ",".join(self.arr_wins)
            self.send_data(self.arrW, self.client_socket)
            data_wins = self.recv_data(self.client_socket)
            arr_wins = data_wins.split(",")
            print(arr_wins)
            if arr_wins[1] == 'GotWins':
                self.winsLBL.set(str(arr_wins[0]))
        except:
            print("error in refreshing")
            return False


    def send_data(self, data, client_socket, state = "NotEncrypted"):
        try:
            print()
            print("*******SsendS**********")
            if state == "zofen":
                print(data)
                data = self.encrypt_message(data)
                print(data)
                data = b"codesodi" + data
                print(data)
            print("The message is: " + str(data))
            length = str(len(data)).zfill(SIZE)
            length = length.encode(self.format)
            print(length)
            if type(data) != bytes:
                data = data.encode()
            print(data)
            msg = length + data
            print("message with length is " + str(msg))
            client_socket.send(msg)
            print("*******EsendE**********")
            print()
        except:
            print("Error with sending msg")





    def recv_data(self, client_socket, ret_type="string"):  # ret_type is string by default unless stated otherwise
        #try:
        print()
        print("*******SrecvS**********")
        length = client_socket.recv(SIZE).decode(self.format) # 00000003tom
        if not length:
            print("NO LENGTH!")
            return None
        print("The length is " + length)
        data = b""
        remaining = int(length)
        while remaining > 0:
            chunk = client_socket.recv(remaining)
            if not chunk:
                print("NO DATA!")
                return None
            data += chunk
            remaining -= len(chunk)
        print("The data is: " + str(data))
        if ret_type == "string":
            data = data.decode(self.format)
        elif ret_type == "pickle":
            data = pickle.loads(data)
        print(data)
        print("*******ErecvE**********")
        print()
        return data
        #except:
            #print("Error with receiving msg")



    def encrypt_message(self, message):
        try:
            # Create a cipher object with the public key
            print(type(self.dataPuKey))
            public_key = RSA.import_key(self.dataPuKey)
            cipher = PKCS1_OAEP.new(public_key)
            # Encrypt the message
            encrypted_message = cipher.encrypt(message.encode())
            return encrypted_message
        except:
            print("error in encrypting...")
            return False






if __name__ == "__main__":
    app = Menu_Screen()
    app.mainloop()