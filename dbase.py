import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("Muhammadjon.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            create table if not exists user(
                id integer primary key ,
                first_name varchar ,
                lastname varchar,
                emailadress varchar,
                phonenumber integer)
        """)

    def insert_user(self, firstname, lastname, emailadress, phonenumber):
        self.cursor.execute("insert into user (first_name, lastname, emailadress, phonenumber) values (?, ?, ?, ?)",
                            (firstname, lastname, emailadress, phonenumber))
        self.connection.commit()

    def read_all_user(self):
        users = self.cursor.execute("select * from user").fetchall()
        return users

    def get_user(self, id):
        user = self.cursor.execute("select * from user where id=?", (id,)).fetchone()
        return user

    def update_user(self, id, firstname, lastname, emailadress, phonenumber):
        self.cursor.execute("update user set firstname=?, lastname=?, emailadress=?, phonenumber=? where id=?",
                            (id, firstname, lastname, emailadress, phonenumber))
        self.connection.commit()

    def delete_user(self, id):
        self.cursor.execute("delete from user where id=?", (id,))
        self.connection.commit()





