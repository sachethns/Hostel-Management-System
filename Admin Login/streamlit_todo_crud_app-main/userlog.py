import streamlit as st
import pandas as pd
from db_fxns import *

import streamlit.components.v1 as stc


HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <p style="color:white;text-align:center;">USER LOG</p>
    </div>
    """


def userlog():
	stc.html(HTML_BANNER)

	menu = ["Read"]
	choice = st.sidebar.selectbox("Menu", menu)
	create_table_userlog()

	if choice == "Create":
		st.subheader("Add Item")
		col1,col2 = st.columns(2)
		
		with col1:
			id = st.text_input("ID")
			userId=st.text_input("User Id ")
			userEmail=st.text_input("User Email")
			password = st.text_input("Password")
			city=st.text_input("City")
			country=st.text_input("Country")
			logindate=st.date_input("Login Date")
 
        
           
		
		
# song_id,song_name,song_format,singer_name,movie_name,movie_name,song_image,audio_file
		
			

		

		if st.button("submit"):
			add_data_userlog(id,userId,userEmail,password,city,country,logindate)
			st.success("Added ::{} ::To Userlog".format(id))


	elif choice == "Read":
		st.subheader("View Userlog")
		with st.expander("View All"):
			result = view_all_data_userlog()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","userId","userEmail","password","city","country","logindate"])
			st.dataframe(clean_df)

	# 	# with st.expander("Task Status"):
	# 	# 	task_df = clean_df['Status'].value_counts().to_frame()
	# 	# 	# st.dataframe(task_df)
	# 	# 	task_df = task_df.reset_index()
	# 	# 	st.dataframe(task_df)

	# 	# 	p1 = px.pie(task_df,names='index',values='Status')
	# 	# 	st.plotly_chart(p1,use_container_width=True)
"""

	elif choice == "Update":
		st.subheader("Edit Items")
		with st.expander("Current Data"):
			result = view_all_data_userlog()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","userId","userEmail","city","country","logindate"])
			st.dataframe(clean_df)

		list_of_user_id = [i[0] for i in view_all_data_userlog()]
		selected_user_id = st.selectbox("id",list_of_user_id)
		user_id_result = get_loggeduser_id(selected_user_id)
		# st.write(user_id_result)

		if user_id_result:
			id = user_id_result[0][0]
			userId = user_id_result[0][1]
			userEmail = user_id_result[0][2]
			city=user_id_result[0][3]
			country=user_id_result[0][4]
			logindate=user_id_result[0][5]

			col1,col2 = st.columns(2)
			
			with col1:
				new_id = st.text_input("Unique id",id)

			with col2:
				new_userId = st.text_input("User ID",userId)
				new_userEmail=st.text_input("Email",userEmail)
				new_city=st.text_input("City",city)
				new_country=st.text_input("Country",country)
				new_logindate=st.date_input("Login Date",logindate)

			if st.button("Update Task"):
				edit_userlog_data(new_id,new_userId,new_userEmail,new_city,new_country,new_logindate,id,userId,userEmail,city,country,logindate)
				st.success("Updated ::{} ::To {}".format(id,new_id))

			with st.expander("View Updated Data"):
				result = view_all_data_userlog()
				# st.write(result)
				clean_df = pd.DataFrame(result,columns=["id","userId","userEmail","city","country","logindate"])
				st.dataframe(clean_df)


	elif choice == "Delete":
		st.subheader("Delete")
		with st.expander("View Data"):
			result = view_all_data_userlog()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","userId","userEmail","city","country","logindate"])
			st.dataframe(clean_df)

		unique_list = [i[0] for i in view_all_userlog()]
		delete_by_id =  st.selectbox("Select Userlog",unique_list)
		if st.button("Delete"):
			delete_userlog_data(delete_by_id)
			st.warning("Deleted: '{}'".format(delete_by_id))

		with st.expander("Updated Data"):
			result = view_all_data_userlog()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","userId","userEmail","city","country","logindate"])
			st.dataframe(clean_df)

	# else:
	# 	st.subheader("About ToDo List App")
	# 	st.info("Built with Streamlit")
	# 	st.info("Jesus Saves @JCharisTech")
	# 	st.text("Jesse E.Agbe(JCharis)")
"""

if __name__ == '__main__':
	main()

