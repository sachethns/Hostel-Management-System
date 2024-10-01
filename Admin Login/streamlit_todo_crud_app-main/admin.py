import streamlit as st
import pandas as pd
from db_fxns import *

import streamlit.components.v1 as stc


HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <p style="color:white;text-align:center;">ADMIN DETAILS</p>
    </div>
    """


def admin():
	stc.html(HTML_BANNER)

	menu = ["Create", "Read", "Update"]
	choice = st.sidebar.selectbox("Menu", menu)
	create_table_admin()

	if choice == "Create":
		st.subheader("Add Details")
		col1,col2 = st.columns(2)
		
		with col1:
			id = st.number_input("Admin ID")
			username=st.text_input("Username")
			email=st.text_input("Email")
			password=st.text_input("Password")
			reg_date=st.date_input("Registration Date")
			updation_date=st.date_input("Updation Date")
            

 
        
           
		
		
# course_id,course_name,course_format,singer_name,movie_name,movie_name,course_image,audio_file
		
			

		

		if st.button("Submit"):
			add_data_admin(id,username,email,password,reg_date,updation_date)
			st.success("Added ::{} ::To Admin".format(id))


	elif choice == "Read":
		st.subheader("View Admin Details")
		with st.expander("View All"):
			result = view_all_data_admin()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","username","email","password","reg_date","updation_date"])
			st.dataframe(clean_df)

	# 	# with st.expander("Task Status"):
	# 	# 	task_df = clean_df['Status'].value_counts().to_frame()
	# 	# 	# st.dataframe(task_df)
	# 	# 	task_df = task_df.reset_index()
	# 	# 	st.dataframe(task_df)

	# 	# 	p1 = px.pie(task_df,names='index',values='Status')
	# 	# 	st.plotly_chart(p1,use_container_width=True)


	elif choice == "Update":
		st.subheader("Edit Details")
		with st.expander("Current Data"):
			result = view_all_data_admin()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","username","email","password","reg_date","updation_date"])
			st.dataframe(clean_df)

		list_of_admin_id = [i[0] for i in view_all_admin()]
		selected_admin_id = st.selectbox("ID",list_of_admin_id)
		admin_id_result = get_admin_id(selected_admin_id)
		# st.write(user_id_result)

		if admin_id_result:
			id = admin_id_result[0][0]
			username = admin_id_result[0][1]
			email = admin_id_result[0][2]
			password = admin_id_result[0][3]
			reg_date = admin_id_result[0][4]
			updation_date = admin_id_result[0][5]

			col1,col2 = st.columns(2)
			
			with col1:
				new_id = st.number_input("Admin id",id)

			with col2:
				new_username = st.text_input("Username",username)
				new_email=st.text_input("Email",email)
				new_password=st.text_input("Password",password)
				new_reg_date=st.date_input("Registration date",reg_date)
				new_updation_date=st.date_input("Updation date",updation_date)

			if st.button("Update Details"):
				edit_admin_data(new_id,new_username,new_email,new_password,new_reg_date,new_updation_date,id,username,email,password,reg_date,updation_date)
				st.success("Updated ::{} ::To {}".format(id,new_id))

			with st.expander("View Updated Data"):
				result = view_all_data_admin()
				# st.write(result)
				clean_df = pd.DataFrame(result,columns=["id","username","email","password","reg_date","updation_date"])
				st.dataframe(clean_df)


	elif choice == "Delete":
		st.subheader("Delete")
		with st.expander("View Data"):
			result = view_all_data_admin()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","username","email","password","reg_date","updation_date"])
			st.dataframe(clean_df)

		unique_list = [i[0] for i in view_all_admin()]
		delete_by_admin_id =  st.selectbox("Select Admin",unique_list)
		if st.button("Delete"):
			delete_admin_data(delete_by_admin_id)
			st.warning("Deleted: '{}'".format(delete_by_admin_id))

		with st.expander("Updated Data"):
			result = view_all_data_admin()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","username","email","password","reg_date","updation_date"])
			st.dataframe(clean_df)

	# else:
	# 	st.subheader("About ToDo List App")
	# 	st.info("Built with Streamlit")
	# 	st.info("Jesus Saves @JCharisTech")
	# 	st.text("Jesse E.Agbe(JCharis)")


if __name__ == '__main__':
	main()

