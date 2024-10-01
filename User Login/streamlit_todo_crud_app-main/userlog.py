import streamlit as st
import pandas as pd
from db_fxns import *

import streamlit.components.v1 as stc


HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <p style="color:white;text-align:center;">LOGIN</p>
    </div>
    """


def userlog():
	stc.html(HTML_BANNER)

	create_table_userlog()

	st.subheader("User Login")
	col1,col2 = st.columns(2)
		
	with col1:
		id = st.text_input("ID")
		userId=st.text_input("User Id ")
		userEmail=st.text_input("User Email")
		password = st.text_input("Password")
		city=st.text_input("City")
		country=st.text_input("Country")
		logindate=st.date_input("Login Date")
 
        
	if st.button("Submit"):
		if(check_user_password(userEmail,password)==True):
			st.success("Successfully logged in   : {}".format(userEmail))
			add_data_userlog(id,userId,userEmail,password,city,country,logindate)
			st.subheader("My Profile")
			with st.expander("View"):
				result = get_registration_detail(userEmail)
				clean_df = pd.DataFrame(result,columns=["id","roomno","seater","feespm","foodstatus","stayfrom","duration","course","regno","firstName","middleName","lastName","gender","contactno","emailid","egycontactno","guardianName","guardianRelation","guardianContactno","corresAddress","corresCIty","corresState","corresPincode","pmntAddress","pmntCity","pmnatetState","pmntPincode","postingDate","updationDate"])
				st.dataframe(clean_df.iloc[0])






if __name__ == '__main__':
	main()

