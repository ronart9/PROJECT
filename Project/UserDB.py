import sqlite3
import hashlib

class UserDB(object):
    def __init__(self, tablename = "Users", Id = "Id", email = "email", password = "password", username ="username", countwins= "countwins"):
        self.__tablename = tablename
        self.__Id = Id
        self.__email = email
        self.__password = password
        self.__username = username
        self.__countwins= countwins

        conn = sqlite3.connect('test.db')
        print ("Opened database successfully")
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
    def select_all_users(self):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            str1 = "select*from " + self.__tablename
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
            #salt = 'SltKey'
            #slt_pass = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
            #print(slt_pass)
            str_insert = f"INSERT INTO {self.__tablename} ({self.__email}, {self.__password}," \
                         f"{self.__username}, {self.__countwins}) VALUES ('{email}', '{password}'," \
                         f" '{username}', '{0}')"
            print(str_insert)
            conn.execute(str_insert)
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
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__email + "=" + "'"+str(email)+"'"
            print(str_delete)
            conn.execute(str_delete)
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
            #salt= 'SltKey'
            #slt_password= hashlib.md5(salt.encode('utf-8')+ password.encode('utf-8')).hexdigest()
            #print(slt_password)
            strsql = "SELECT * from " + self.__tablename + " where " + self.__email + "=" + "'" + str(email) + "'" + " and " + self.__password + "=" + "'" + password + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            print(cursor)
            row= cursor.fetchone()
            print(row)
            user_data = str([row[1], row[2], row[3], row[4]])
            print("User data: " + str(user_data))
            conn.commit()
            conn.close()

            return row[3]
        except:
            print("failed")
            return False

    def log_in(self, email, password):
        try:
            conn = sqlite3.connect('test.db')
            strsql = "SELECT * FROM " + self.__tablename + " WHERE " + self.__email + "=" + "'" + str(email) + "'"+ " and " + self.__password + "=" + "'" + str(password) + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            conn.commit()
            conn.close()
            if row:
                print("success")
                return True
            else:
                print("Failed to find user")
                return False
        except:
            return False

       # except:
            #messagebox.showerror("error message", "Error")
            #return



    def __str__(self):
        return "table  name is ", self.__tablename


#u=UserDB()
#u.insert_user("u@x.com", "oron", 'yaron', 69)
#u.insert_user("v@y.com", "dvidi", 'davidi')
#u.insert_user("t@a.com", "aba", 'origin')
#u.select_all_users()
#u.check_user_by_username("Asaf")
#u.delete_username("Asaf")
#u.check_user_by_username("Asaf")
#user=u.return_user_by_email('tom@g', "123")
#print(user[0])
#print(user)
#end
