import threading
import tkinter
from tkinter import *
from Register import Register
#from login import Login
import socket
#from users import User
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

from tkinter import ttk
#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'

class Menu_Screen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1200x600')
        self.resizable(width=False, height=False)
        self.title('Main Window')
        #self.img = Image.open('one piece.jpg')
        #self.resize = self.img.resize((600, 450), Image.Resampling.LANCZOS)
        #self.imgLabel = Label(self, image=self.bg)
        #self.imgLabel.pack(expand=YES)
        # place a button on the root window
        #self.btn_register = Button(self, text='Register', command=self.open_register, background="green")
        #self.btn_register.place(x=200, y=50)
        self.create_gui()

    def create_gui(self):
        self.configure(bg='#856ff8')  # -using color HEX
        self.lab_email= Label(self, text='Enter Email: ', font =('Helvetica bold',15))
        self.lab_email.place(x= 100, y= 120)
        self.ent_email= Entry(self, font= 30)
        self.ent_email.place(x= 100, y= 165)
        self.lab_password = Label(self, text='Enter Password: ', font =('Helvetica bold',15))
        self.lab_password.place(x=100, y=235)
        self.ent_password = Entry(self, show= "*", font= 30)
        self.ent_password.place(x=100, y=280)
        self.btn_login = Button(self, text='Login', command=self.log_in, font= 30, background="#b7f061")
        self.btn_login.place(x=100, y=350)
        self.btn_regiser = Button(self, text='Register', command=self.open_register, font=30, background="#ffd966")
        self.btn_regiser.place(x=100, y=420)
        #self.plz = StringVar()
        #self.lab_plz_login = Label(self, textvariable=self.plz, background="yellow")
        #self.lab_plz_login.place(x=100, y=420)

        self.handle_thread_socket()



    #def open_register(self):
        #window = Register(self)
        #window.grab_set()
        #self.withdraw()

    #def open_login(self):
        #Login(self)
        #window = Login(self)
        #window.grab_set()
        #self.withdraw()
    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()

    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 1802))
        data = self.client_socket.recv(1024).decode()
        print("data"+data)
        print("hi", self.client_socket)

    def log_in(self):
        try:
            email = self.ent_email.get()
            password= self.ent_password.get()
            arr = ["login", email, password]
            insert= ",".join(arr)
            print(insert)
            self.client_socket.send(insert.encode())
            data= self.client_socket.recv(1024).decode()
            d= str(data)
            if d[0]== 'W':
                self.plz.set(data)
                print(data)
            elif d[0]== 'F':
                self.plz.set(data)
                messagebox.showerror("error message", "Error")
                print(data)
            return data
        except:
            return False


    def open_register(self):
        window = Register(self)
        window.grab_set()
        self.withdraw()

if __name__ == "__main__":
    app = Menu_Screen()
    app.mainloop()