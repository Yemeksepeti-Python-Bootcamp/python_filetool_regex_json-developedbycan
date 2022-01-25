import sqlite3
from datetime import datetime
from parse_json import ParseJson


class DbOpen:
    """
    Contex Manager for sqlite3 databases. It allows to connect and exit database properly.
    The common used example of contex manager is the with statement.
    """
    def __init__(self, db_path):
        """
        For this method, all that needs to be done is to store the db_path parameter value
        into  a self.db_path variable
        :param db_path: database path as string
        :return: Use it in the __enter__() method
        """
        self.db_path = db_path

    def __enter__(self):
        """
        __enter__ represents the method that is called when a class object of DbOpen is used wihtin a "with"
        This method will start the connection to SQLite database indicated by self.db_path
        :return: self.cursor for with statement
        """
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        __exit__ represents the method is called after the last line of a with block is executed.
        This method will commit connection, show data inserted the database and close the database connection.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return: commit and close
        """
        """commit"""
        self.conn.commit()
        print(f"{self.cursor.rowcount} tane kayit eklendi.")
        """show data inserted the database"""
        sql = f"Select * From data_{datetime.strftime(datetime.today(), '%Y%m%d')}"
        self.cursor.execute(sql)
        for user in self.cursor.fetchall():
            print(user)
        """close databese connection"""
        self.conn.close()
        print("Database baglantisi kapandi.")


def db_helper(db_path, json_file):
    """
    This function helps to create table and insert data via "with" statemant.
    This function is gonna be called in the main file. In order to use "with" statement in main file,
    I created this function.
    :param db_path: database path as a string
    :param json_file: json file
    :return: helps to use "with" statement
    """
    with DbOpen(db_path) as cursor:
        """create table"""

        table_name = f"data_{datetime.strftime(datetime.today(), '%Y%m%d')}"
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                id TEXT PRIMARY KEY,
                                email TEXT NOT NULL,
                                username TEXT NOT NULL,
                                fullname TEXT NOT NULL,
                                emailuserlk INT NOT NULL,
                                usernamelk INT NOT NULL,
                                year INT NOT NULL,
                                month INT NOT NULL,
                                day INT NOT NULL,
                                city TEXT NOT NULL,
                                ap INT NOT NULL);""")

        """insert users data came from json file into database """

        obj = ParseJson(json_file)
        data_list = obj.get_list()
        sql = f"""INSERT OR REPLACE INTO {table_name} (
                                       id,email,username,fullname,
                                       emailuserlk,usernamelk,
                                       year,month,day,city,ap) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        values = []
        user_obj_list = data_list
        for user in user_obj_list:
            values.append((user.user_id, user.email, user.user_name, user.name, user.emailuserlk, user.usernamelk,
                           user.year, user.month, user.day, user.city, user.ap))
        cursor.executemany(sql, values)















