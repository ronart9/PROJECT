import multiprocessing
import socket
import threading
from UserDB import *
import hashlib
from Player import *

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
                client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSocket,))
                client_handler.start()

        except socket.error as e:
            print(e)

    #def handleClient(self, clientSock, current):
        #client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current,))
        #client_handler.start()

    def handle_client_connection(self, client_socket):
        not_crash = True
        print(not_crash)
        while not_crash:
            print("____________________")
            try:
                server_data = client_socket.recv(1024).decode()
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
                        client_socket.send(username.encode())
                        messege = "Welcome: [ " + str(username) + " ]"
                        client_socket.send(messege.encode())
                    elif not username:
                        # messagebox.showerror("error message", "Error")
                        client_socket.send("Failed !".encode())
                        client_socket.send("Failed to Login !".encode())

                elif arr and arr[0] == "JoinLobby" and len(arr) == 2:
                    print("Lobby...")
                    self.Create_Lobby(client_socket, arr)

                elif arr and arr[0] == "LeaveLobby" and len(arr) == 2:
                    self.leaveLobby(client_socket, arr)

                elif arr and arr[0] == "UserNameP2" and len(arr) == 2:
                    if (arr[1] == self.players[0].name):
                        self.SendPlayerName1(client_socket, arr)
                    elif (arr[1] == self.players[1].name):
                        self.SendPlayerName2(client_socket, arr)

                elif arr and arr[0] == "Rounds" and len(arr) == 3:
                    if(arr[1] == self.players[0].name and arr[2] != "11"):
                        self.Count_Rounds1(client_socket, arr)
                    elif (arr[1] == self.players[1].name and arr[2] != "11"):
                        self.Count_Rounds2(client_socket, arr)



                elif arr and arr[0] == "WinScreen" and len(arr) == 2:
                    if (arr[1] == self.players[0].name):
                        self.Win_Screen1(client_socket, arr)
                        self.Win_Screen2(client_socket, arr)
                        self.winner = self.players[0].name
                        self.loser = self.players[1].name
                    elif (arr[1] == self.players[1].name):
                        self.Win_Screen1(client_socket, arr)
                        self.Win_Screen2(client_socket, arr)
                        self.winner = self.players[1].name
                        self.loser = self.players[0].name
                    print(self.winner)
                    print(self.loser)

                elif arr and arr[0] == "Winner_Loser" and len(arr) == 1:
                    arr_winner_loser = [str(self.winner), str(self.loser), "Win_Lose_Players"]
                    str_winner_loser = ",".join(arr_winner_loser)
                    client_socket.send(str_winner_loser.encode())


                elif arr != None and arr[0] == "get_all_users" and len(arr) == 1:
                    print("get_all_users")
                    server_data = self.userDb.select_all_users()
                    server_data = ",".join(server_data)  # convert data to string
                else:
                    server_data = "Failed"
                    client_socket.send(server_data.encode())
            except:
                print("error")
                not_crash = False
                break


    def Create_Lobby(self, client_socket, arr):
        player = Player(client_socket, arr[1])
        self.players.append(player)
        if(len(self.players) == 1):
            data = [arr[1], "wait"]
            join_data = ",".join(data)
            client_socket.send(join_data.encode())
        elif(len(self.players) == 2):
            player1 = self.players[0]
            player2 = self.players[1]
            socket1 = player1.client_socket
            socket2 = player2.client_socket
            data1 = [player1.name, "start"]
            data2 = [player2.name, "start"]
            str_data1 = ",".join(data1)
            str_data2 = ",".join(data2)
            socket1.send(str_data2.encode())
            socket2.send(str_data1.encode())


    def leaveLobby(self, client_socket, arr):
        while True:
            print(arr[1])
            if(arr[1] == self.players[0].name):
                self.players.remove(self.players[0])
                self.players[1].send("playerleave".encode())
            elif (arr[1] == self.players[1].name):
                self.players.remove(self.players[1])
                self.players[0].send("playerleave".encode())

    def SendPlayerName1(self, client_socket, arr):
        player2 = self.players[1]
        socket2 = player2.client_socket
        dataname2 = [str(self.players[0].name), "DataName"]
        str_dataname2 = ",".join(dataname2)
        socket2.send(str_dataname2.encode())

    def SendPlayerName2(self, client_socket, arr):
        player1 = self.players[0]
        socket1 = player1.client_socket
        dataname1 = [str(self.players[1].name), "DataName"]
        str_dataname1 = ",".join(dataname1)
        socket1.send(str_dataname1.encode())


    def Win_Screen1(self, client_socket, arr):
        # "CloseWindowGame"
        player2 = self.players[1]
        socket2 = player2.client_socket
        dataname2 = [str(self.players[0].name), "CloseWindowGame"]
        str_dataname2 = ",".join(dataname2)
        socket2.send(str_dataname2.encode())

    def Win_Screen2(self, client_socket, arr):
        player1 = self.players[0]
        socket1 = player1.client_socket
        dataname1 = [str(self.players[1].name), "CloseWindowGame"]
        str_dataname1 = ",".join(dataname1)
        socket1.send(str_dataname1.encode())


    def Count_Rounds1(self, client_socket, arr):
        player2 = self.players[1]
        socket2 = player2.client_socket
        data = [arr[2], "This_Round", arr[1]]
        str_data1 = ",".join(data)
        socket2.send(str_data1.encode())


    def Count_Rounds2(self, client_socket, arr):
        player1 = self.players[0]
        socket1 = player1.client_socket
        data = [arr[2], "This_Round", arr[1]]
        str_data1 = ",".join(data)
        socket1.send(str_data1.encode())

    def Win_Loser_P1(self, client_socket, arr):
        player2 = self.players[1]
        socket2 = player2.client_socket
        arr_winner_loser = [str(self.winner), str(self.loser), "Win_Lose_Players"]
        str_winner_loser = ",".join(arr_winner_loser)
        socket2.send(str_winner_loser.encode())

    def Win_Loser_P2(self, client_socket, arr):
        player1 = self.players[0]
        socket1 = player1.client_socket
        arr_winner_loser = [str(self.winner), str(self.loser), "Win_Lose_Players"]
        str_winner_loser = ",".join(arr_winner_loser)
        socket1.send(str_winner_loser.encode())


        #arr_winner_loser = [str(self.winner), str(self.loser), "Win_Lose_Players"]
        #str_winner_loser = ",".join(arr_winner_loser)
        #socket1.send(str_winner_loser.encode())
        #socket2.send(str_winner_loser.encode())

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1802
    s = Server(ip, port)
    s.start()
