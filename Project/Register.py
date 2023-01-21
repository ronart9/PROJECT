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


    def create_gui(self):
        self.configure(bg='#ffc892')  # -using color HEX
        #----------------------------------------------------------------------------------------------
        self.lbl_email = Label(self, text="Email :", font =('Helvetica bold',15), bg='#ffc892')
        self.lbl_email.place(x=180, y=100)
        self.email = Entry(self, font=30)
        self.email.place(x=180, y=150)
        #----------------------------------------------------------------------------------------------
        self.lbl_password = Label(self, text="Password :", font =('Helvetica bold',15), bg='#ffc892')
        self.lbl_password.place(x=180, y=200)
        self.password = Entry(self, font=30)
        self.password.place(x=180, y=250)
        #----------------------------------------------------------------------------------------------
        self.lbl_username = Label(self, text="Username :", font =('Helvetica bold',15), bg='#ffc892')
        self.lbl_username.place(x=180, y=300)
        self.username = Entry(self, font=30)
        self.username.place(x=180, y=350)
        #----------------------------------------------------------------------------------------------
        self.btn_close= Button(self, text='Close', command=self.close, font =('Helvetica bold',12), background= "#ea1111")
        self.btn_close.place(x= 560, y= 50)
        #----------------------------------------------------------------------------------------------
        self.buttonPlus = Button(self, text="register", command=self.handle_add_user, font=30, background="green")
        self.buttonPlus.place(x=180, y=400)
        #----------------------------------------------------------------------------------------------
        self.img_adress = "garbage.png"
        self.imggarbage = Image.open(self.img_adress)
        self.resized = self.imggarbage.resize((35, 35), Image.Resampling.LANCZOS)
        self.garbage = ImageTk.PhotoImage(self.resized)
        self.btn_clear = Button(self, text='Clear', command=self.clear_text, font=('Helvetica bold', 12), image=self.garbage)  # background= "#f86060"
        self.btn_clear.place(x=300, y=400)
        #----------------------------------------------------------------------------------------------



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

    def clear_text(self):
        self.email.delete(0, END)
        self.password.delete(0, END)
        self.username.delete(0, END)