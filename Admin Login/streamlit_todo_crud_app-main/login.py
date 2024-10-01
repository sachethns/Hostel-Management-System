import streamlit as st
import pandas as pd 
from db_fxns import * 

import streamlit.components.v1 as stc



HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <p style="color:white;text-align:center;">LOGIN</p>
    </div>
    """


def admin_login():
    stc.html(HTML_BANNER)
    st.subheader("Sign In")
    username=st.text_input("Username")
    password=st.text_input("Password")
    if st.button("Submit"):
        if(check_admin_password(username,password)==True):
            st.success("Successfully logged in   : {}".format(username))
            #posts(name)
            return username

def user_login():
    stc.html(HTML_BANNER)
    st.subheader("Sign In")
    email=st.text_input("Email")
    password=st.text_input("Password")
    if st.checkbox("Submit"):
        if(check_user_password(email,password)==True):
            st.success("Successfully logged in   : {}".format(email))
            #posts(name)
            return email
	

if __name__ == '__main__':
	main()




