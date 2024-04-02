from Functions import *
import streamlit as st

from Functions import *
from Functions import check_login, check_repeat


def login():

    if "disabled" not in st.session_state:
        st.session_state["disabled"] = False

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('')
    with col2:
        st.image('https://www.mmipromo.com/commercebankstore/images/themes/CommerceBank.jpg', width=200)
    with col3:
        st.write('')

    menu = ['Login', 'New User']
    choice = st.selectbox("Select a Login Option", menu, disabled=st.session_state.disabled)

    if choice == 'Login':

        st.markdown("<h1 style='text-align: left; color: black; font-size: 30px'> Login: </h1>", unsafe_allow_html=True)

        userName = st.text_input('Email: ', disabled=st.session_state.disabled)
        password = st.text_input('Password: ', disabled=st.session_state.disabled)

        if st.button('Submit'):
            if len(userName) == 0:
                st.write("Username space cannot be empty")
            elif len(password) == 0:
                st.write("Password cannot be empty")
            else:
                #st.write("Submit button hit")
                if check_login(userName, password) == '0':
                    st.write("Password is incorrect")
                elif check_login(userName, password) == '1':
                    st.write("Username and/or Password are incorrect")
                else:
                    fname, lname = check_login(userName, password)
                    st.session_state["logged in"] = True
                    #st.write("Welcome back: " + check_login(userName, password))


    if choice == "New User":

        st.markdown("<h1 style='text-align: center; color: black;'> New User </h1>", unsafe_allow_html=True)

        st.markdown("<h1 style='text-align: left; color: black; font-size: 30px'> Personal Information: </h1>",
                    unsafe_allow_html=True)
        firstName = st.text_input('First Name: ')
        lastName = st.text_input('Last Name: ')
        userName = st.text_input('Email: ')
        password = st.text_input('Create Password: ')
        password2 = st.text_input("Re-enter Password")
        st.markdown("<h1 style='text-align: left; color: black; font-size: 30px'> Security Questions: </h1>",
                    unsafe_allow_html=True)
        st.write("Security Question 1:")
        q1 = st.text_input("What is your favorite animal?")
        st.write("Security Question 2:")
        q2 = st.text_input("What is your favorite dessert?")
        st.write("Security Question 3:")
        q3 = st.text_input("What is your favorite sport")

        if st.button('Register'):
            check_repeat(userName)
            if lastName == "" or firstName == "" or password == "":
                st.write("User Information cannot be blank")
            elif q1 == "" or q2 == "" or q3 == "":
                st.write("User Questions cannot be blank")
            elif password != password2:
                st.write("Passwords do not match")
            else:
                print("Registered Info")
                if check_repeat(userName) == False:
                    st.write("Email already taken")
                elif check_repeat(userName) == True:
                    #st.write("F: Email not taken")
                    add_to_database(firstName, lastName, userName, password, q1, q2, q3)
                    st.write("User has been added to database")





