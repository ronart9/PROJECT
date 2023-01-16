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
        self.geometry('700x600')
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
        self.btn_close.place(x= 100, y= 470)

    def create_gui(self):
        self.configure(bg='#ffc892')  # -using color HEX

        self.lbl_email = Label(self, width=10, text="Email :", font =('Helvetica bold',15))
        self.lbl_email.place(x=180, y=100)
        self.email = Entry(self, font=30)
        self.email.place(x=180, y=150)

        self.lbl_password = Label(self, width=10, text="Password :", font =('Helvetica bold',15))
        self.lbl_password.place(x=180, y=200)
        self.password = Entry(self, font=30)
        self.password.place(x=180, y=250)

        self.lbl_username = Label(self, width=10, text="Username :", font =('Helvetica bold',15))
        self.lbl_username.place(x=180, y=300)
        self.username = Entry(self, font=30)
        self.username.place(x=180, y=350)



        self.buttonPlus = Button(self, text="register", command=self.handle_add_user, font=30, background="green")
        self.buttonPlus.place(x=180, y=400)

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.register_user, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def register_user(self):

        if len(self.email.get())==0:
            messagebox.showerror("please write email name", "Error")
            return
        print("register")
        arr = ["register", self.email.get(), self.password.get(), self.username.get()]
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