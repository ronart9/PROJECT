import sqlite3


class GameDB:
    def __init__(self, tablename="GamesDB", id="ID", player1="Player1", player2="Player2", playerwin="Winner"):
        self.__tablename = tablename
        self.__id = id
        self.__player1 = player1
        self.__player2 = player2
        self.__playerwin = playerwin

        conn = sqlite3.connect('gamesdb.db')
        print("Opened database successfully")
        str1 = f"CREATE TABLE IF NOT EXISTS {self.__tablename} ({self.__id} INTEGER PRIMARY KEY AUTOINCREMENT,"
        str1 += f" {self.__player1} TEXT NOT NULL,"
        str1 += f" {self.__player2} TEXT NOT NULL,"
        str1 += f" {self.__playerwin} TEXT NOT NULL)"
        conn.execute(str1)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def insert_game(self, player1, player2, winner):
        try:
            conn = sqlite3.connect('gamesdb.db')
            print("Opened database successfully")
            str_insert = f"INSERT INTO {self.__tablename} ({self.__player1}, {self.__player2}, {self.__playerwin})"
            str_insert += " VALUES (?, ?, ?)"
            print(str_insert)
            conn.execute(str_insert, (player1, player2, winner))
            conn.commit()
            conn.close()
            print("Record created successfully")
            return True
        except:
            print("Failed to insert game")
            return False

    def get_history(self):
        try:
            conn = sqlite3.connect('gamesdb.db')
            print("Opened database successfully")
            str1 = "select*from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_games = []
            for row in rows:
                str_rows = str(row[0]) + " " + row[1] + " " + row[2] + " " + row[3]
                arr_games.append(str_rows)
            print(arr_games)
            return arr_games
        except:
            print("failed - get games")
            return False