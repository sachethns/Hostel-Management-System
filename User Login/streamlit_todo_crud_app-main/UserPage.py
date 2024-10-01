  
import streamlit as st
import mysql.connector

from register import register
from login import *
from state import state
from room import room
from userlog import userlog
from course import courses
from admin import admin
from registration import registration

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
	database="hostel"
)
c = mydb.cursor()

def main():
    st.title("Hostel Management System")
    menu = ["User Registration","Login & View Profile","Room Details"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice=="Login & View Profile":
        userlog()
    if choice=="User Registration":
        register()  
    elif choice=="Room Details":
        room()
    # elif choice=="list user":
    #     read_all()
    # elif choice=="posts tweet":
    #     posts()
    # elif choice=="follow":
    #     follows()
    # elif choice=="Show Friends":
    #     friends()
    # elif choice=="Show Tweets":
    #     showtweets()
    # else:
    #     username=login()
    #     if 'username' not in st.session_state:
    #         print(username)
    #         st.session_state['username']=username
        
if __name__ == '__main__':
    main()



# def read(conn):
#     print("read")
#     cursor=conn.cursor()
#     cursor.execute("select * from USER_INFO")
#     for row in cursor:
#         print(f'roe={row}')
#     print()

# def create(conn):
#     print("Create")
#     cursor=conn.cursor()
#     cursor.execute(
#         'insert into USER_INFO (id,f_name,l_name,age) values(?,?,?,?);',
#         (8,'Pavan','N',20)
#     )
#     conn.commit()
#     read(conn)

