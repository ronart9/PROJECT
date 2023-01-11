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
class Register(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x450')
        self.resizable(width=False, height=False)
        self.title('add user/register')
        #self.img = Image.open('what.jpg')
        #self.resize = self.img.resize((600, 450), Image.Resampling.LANCZOS)
        #self.bg = ImageTk.PhotoImage(self.resize)
        #self.imgLabel = Label(self, image=self.bg)
        #self.imgLabel.pack(expand=YES)
        #self.userdb= User()

        self.create_gui()
        self.btn_close= Button(self, text='Close', command=self.close)
        self.btn_close.place(x= 100, y= 300)

    def create_gui(self):
        # phase 1 button
        self.lbl_email = Label(self, width=10, text="email :")
        self.lbl_email.place(x=100, y=50)
        self.email = Entry(self, width=20)
        self.email.place(x=100, y=80)

        self.lbl_password = Label(self, width=10, text="password :")
        self.lbl_password.place(x=100, y=110)
        self.password = Entry(self, width=20)
        self.password.place(x=100, y=140)

        self.lbl_firstname = Label(self, width=10, text="firstname :")
        self.lbl_firstname.place(x=100, y=170)
        self.firstname = Entry(self, width=20)
        self.firstname.place(x=100, y=200)

        self.buttonPlus = Button(self, text="register", command=self.handle_add_user, width=20, background="green")
        self.buttonPlus.place(x=100, y=250)

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.register_user, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def register_user(self):

        if len(self.email.get())==0:
            messagebox.showerror("please write city name", "Error")
            return
        print("register")
        arr = ["register", self.email.get(), self.password.get(), self.firstname.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)

    # old register user
    # def register_user(self):
    #     if len(self.email.get())==0:
    #         messagebox.showerror("please write city name", "Error")
    #         return
    #     self.userdb.insert_user(self.email.get(), self.password.get(), self.firstname.get())
    def close(self):
        self.parent.deiconify() #show parent
        self.destroy()# close and destroy this screen