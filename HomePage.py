from Functions import *
import streamlit as st


def homePage():
    if st.button("Log Out"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('')
    with col2:
        st.image('https://www.mmipromo.com/commercebankstore/images/themes/CommerceBank.jpg', width=200)
    with col3:
        st.write('')

    add_select = st.sidebar.selectbox(
        "Select an option: ",
        ("Home", "Add Transactions", "View Transactions", "Loan Calculator")
    )

    if add_select == "Home":

        st.markdown("<h1 style='text-align: center; color: black; font-size: 40px'> Home </h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: white; font-size: 20px'> Select an option in the sidebar </h1>", unsafe_allow_html=True)


    if add_select == "Add Transactions":
        st.markdown("<h1 style='text-align: center; color: black; font-size: 40px'> Add Transactions </h1>", unsafe_allow_html=True)

    if add_select == "View Transactions":
        st.markdown("<h1 style='text-align: center; color: black; font-size: 40px'> View Transactions </h1>", unsafe_allow_html=True)

    if add_select == "Loan Calculator":
        st.markdown("<h1 style='text-align: center; color: black; font-size: 40px'> Loan Calculator </h1>", unsafe_allow_html=True)

