import multiprocessing
import socket
import threading
from UserDB import *
import hashlib

class Server(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.count = 0
        self.running = True
        self.userDb = UserDB()
        self.players = []

    def start(self):
        try:

            print('server starting up on ip %s port %s' % (self.ip, self.port))
            # Create a TCP/IP socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.ip, self.port))
            self.sock.listen(2)

            while True:
                print('waiting for a new client')
                clientSocket, client_addresses = self.sock.accept()
                print('new client entered')
                clientSocket.send('Hello this is server'.encode())
                self.count += 1
                print(self.count)
                # implement here your main logic
                client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSocket,self.count))
                client_handler.start()

        except socket.error as e:
            print(e)

    #def handleClient(self, clientSock, current):
        #client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current,))
        #client_handler.start()

    def handle_client_connection(self, client_socket, current):
        not_crash = True
        print(not_crash)
        while not_crash:
            print("____________________")
            #try:
            server_data = client_socket.recv(1024).decode('utf-8')
            if server_data == "":
                break
            # insert,email,password,firstname
            arr = server_data.split(",")
            print(server_data)
            if arr and arr[0] == "register" and len(arr) == 4:
                print("register user")
                print(arr)
                IsExist = self.userDb.insert_user(arr[1], arr[2], arr[3])
                print("server data:", IsExist)
                if IsExist:
                    client_socket.send("success register".encode())
                elif IsExist:
                    client_socket.send("failed register".encode())
            elif arr and arr[0] == "login" and len(arr) == 3:
                print(arr)
                username = self.userDb.return_user_by_email(arr[1], arr[2])
                print("Server data: ", username)
                if username:
                    messege = "Welcome: [ " + str(username) + " ]"
                    client_socket.send(messege.encode())
                elif not username:
                    # messagebox.showerror("error message", "Error")
                    client_socket.send("Failed to Login !".encode())

            elif arr and arr[0] == "JoinLobby" and len(arr) == 3:
                while len(self.players) != 2:
                    current = self.count
                    if current == 1:
                        username1 = self.userDb.return_user_by_email(arr[1], arr[2])
                        print(arr)
                        print("Server data: ", username1)
                        if username1:
                            messege = "Player " + str(current) +":" +"\n[ " + str(username1) + " ]"
                            client_socket.send(messege.encode())
                        elif not username1:
                            # messagebox.showerror("error message", "Error")
                            client_socket.send("Failed to find a Player".encode())
                        player1 = [username1, client_socket , current]
                        self.players.append(player1)
                        print(arr[0])
                        print(player1)
                    if current == 2:
                        username2 = self.userDb.return_user_by_email(arr[1], arr[2])
                        print(arr)
                        print("Server data: ", username2)
                        if username2:
                            messege = "Player " + str(current) + ":" + "\n[ " + str(username2) + " ]"
                            client_socket.send(messege.encode())
                        elif not username2:
                            # messagebox.showerror("error message", "Error")
                            client_socket.send("Failed to find a Player".encode())
                        player2 = [username2, client_socket, current]
                        self.players.append(player2)
                        print(arr[0])
                        print(player2)
                    else:
                        current = 0

            elif arr != None and arr[0] == "get_all_users" and len(arr) == 1:
                print("get_all_users")
                server_data = self.userDb.select_all_users()
                server_data = ",".join(server_data)  # convert data to string
            else:
                server_data = "Failed"
                client_socket.send(server_data.encode())
            #except:
                #print("error")
                #not_crash = False
                #break
        self.Create_Lobby()

    def Create_Lobby(self):
        print(self.players)
        player1 = self.players[0]
        print(f"{player1} complete1")
        player2 = self.players[1]
        print(f"{player2} complete2")
        message = "Player 1:\n[ " + str(player1[0]) + " ]"
        message2 = "Player 2:\n[ " + str(player2[0]) + " ]"
        #player2[1].send(message.encode())
        #player1[1].send(message2.encode())



if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1802
    s = Server(ip, port)
    s.start()
