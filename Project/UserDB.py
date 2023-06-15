import sqlite3
import hashlib

class UserDB(object):
    def __init__(self, tablename="Users", Id="Id", email="email", password="password", username="username", countwins="countwins"):
        self.__tablename = tablename
        self.__Id = Id
        self.__email = email
        self.__password = password
        self.__username = username
        self.__countwins = countwins

        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__Id + " " + " INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__email + " TEXT    NOT NULL ,"
        str += " " + self.__password + " TEXT    NOT NULL, "
        str += " " + self.__username + " TEXT    NOT NULL, "
        str += " " + self.__countwins + " INTEGER    NOT NULL)"
        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def get_table_name(self):
        return self.__tablename

    def get_win(self, username):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            strsql = f"SELECT * from {self.__tablename} where {self.__username} = ?"
            print(strsql)
            cursor = conn.execute(strsql, (username,))
            print(cursor)
            row = cursor.fetchone()
            print(row)
            user_data = str([row[1], row[2], row[3], row[4]])
            print("User data: " + str(user_data))
            conn.commit()
            conn.close()

            return row[4]
        except:
            print("Failed")
            return False

    def update_wins(self, username):
        try:
            conn = sqlite3.connect('test.db')
            cur_wins = self.get_win(username)
            updated_wins = int(cur_wins) + 1
            print("new count wins =", updated_wins)
            str_update = f"UPDATE {self.__tablename} SET {self.__countwins} = ? WHERE {self.__username} = ?"
            print(str_update)
            conn.execute(str_update, (updated_wins, username))
            conn.commit()
            conn.close()
            print("Success on updating wins!")
        except:
            print("Failed updating wins!")

    def select_all_users(self):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            str1 = f"SELECT * FROM {self.__tablename}"
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_users = []
            for row in rows:
                str_rows = str(row[0]) + " " + row[1] + " " + str(row[2])
                arr_users.append(str_rows)
            print(arr_users)
            return arr_users
        except:
            return False

    def insert_user(self, email, password, username):
        try:
            conn = sqlite3.connect('test.db')
            salt = 'SltKey'
            slt_pass = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
            print(slt_pass)
            str_insert = f"INSERT INTO {self.__tablename} ({self.__email}, {self.__password}, {self.__username}, {self.__countwins}) VALUES (?, ?, ?, ?)"
            values = (email, slt_pass, username, 0)
            print(str_insert)
            conn.execute(str_insert, values)
            print("1")
            conn.commit()
            print("2")
            conn.close()
            print("Record created successfully")
            return True
        except:
            print("Failed to insert user")
            return False

    def delete_by_firstname(self, email):
        try:
            conn = sqlite3.connect('test.db')
            str_delete = f"DELETE from {self.__tablename} where {self.__email} = ?"
            print(str_delete)
            conn.execute(str_delete, (email,))
            conn.commit()
            conn.close()
            print("Record deleted successfully")
            return "Success"
        except:
            return "Failed to delete user"

    def return_user_by_email(self, email, password):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            salt = 'SltKey'
            slt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
            print(slt_password)
            strsql = f"SELECT * from {self.__tablename} where {self.__email} = ? and {self.__password} = ?"
            values = (email, slt_password)
            print(strsql)
            cursor = conn.execute(strsql, values)
            print(cursor)
            row = cursor.fetchone()
            print(row)
            user_data = str([row[1], row[2], row[3], row[4]])
            print("User data: " + str(user_data))
            conn.commit()
            conn.close()

            return row[3]
        except:
            print("Failed")
            return False

    def log_in(self, email, password):
        try:
            conn = sqlite3.connect('test.db')
            strsql = f"SELECT * FROM {self.__tablename} WHERE {self.__email} = ? and {self.__password} = ?"
            values = (email, password)
            print(strsql)
            cursor = conn.execute(strsql, values)
            row = cursor.fetchone()
            conn.commit()
            conn.close()
            if row:
                print("Success")
                return True
            else:
                print("Failed to find user")
                return False
        except:
            return False

    def __str__(self):
        return "Table name is " + self.__tablename


# Example usage
#u = UserDB()
#u.insert_user("u@x.com", "oron", 'yaron')
#u.select_all_users()
