import mysql.connector
from Login import *

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


def check_login(uName, password):
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM user_info")
    users = mycursor.fetchall()

    for i in range(len(users)):
        if users[i][1] == uName:
            if users[i][2] == password:
                return users[i][0]
            else:
                return '0'

        elif i == len(users) - 1 and users[i][1] != uName:
            return '1'



