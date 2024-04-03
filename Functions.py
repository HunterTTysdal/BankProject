import mysql.connector
from Login import *
import streamlit as st

# To Do
# Disable Login option upon successful login
# When logging out, reset function to original state -> login()
# add drop bar to home page
# in function add connection to sql and add functions to check inputs for login
# recreate tables in sql database to match inputs of front end



connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='G@rfield123',
    port='3306',
    database='bank_data'
)

mycursor = connection.cursor()
mycursor.execute("SELECT * FROM user_info")
users = mycursor.fetchall()


def check_login(uName, pword):
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM user_info")
    users = mycursor.fetchall()

    for i in range(len(users)):
        if users[i][2] == uName:
            if users[i][3] == pword:

                return users[i][0], users[i][1]
            else:
                return '0'

        elif i == len(users) - 1 and users[i][2] != uName:
            return '1'

def check_repeat(email):
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM user_info")
    users = mycursor.fetchall()

    for i in range(len(users)):
        if users[i][2] == email:
            return False
        elif i == len(users) - 1 and users[i][2] != email:
            return True

def add_to_database(first, last, email, password, a1, a2, a3):
    mycursor = connection.cursor()
    query = ("INSERT INTO user_info (fName, lName, email, pword, a1, a2, a3)"
             "VALUES(%s, %s, %s, %s, %s, %s, %s)")
    record = (first, last, email, password, a1, a2, a3)
    mycursor.execute(query, record)
    connection.commit()


