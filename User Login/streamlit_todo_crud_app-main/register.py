import streamlit as st
import pandas as pd 
from db_fxns import * 

import streamlit.components.v1 as stc



HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <p style="color:white;text-align:center;">USER REGISTRATION</p>
    </div>
    """


def register():
	stc.html(HTML_BANNER)

	list_of_regno = [i[8] for i in view_all_data_registration()]
	list_of_gender = ['Male','Female']
	menu = ["Create","Read","Update"]
	choice = st.sidebar.selectbox("Menu",menu)
	create_table_userregistration()

	if choice == "Create":
		st.subheader("Add Details")
		col1,col2 = st.columns(2)
		
		with col1:
			id = st.text_input("ID")
			regNo=st.selectbox("Registration Number",list_of_regno)
			firstName=st.text_input("First Name")
			middleName=st.text_input("Middle Name")
			lastName=st.text_input("Last Name")
			gender=st.selectbox("Gender",list_of_gender)
			contactNo=st.text_input("Contact Number")
			email=st.text_input("Email address")
			password=st.text_input("Password")
			regDate=st.date_input("Registration Date")
			updationDate=st.date_input("Updation Date")
			passUdateDate=st.date_input("Pass Updation Date")

		

		if st.button("User"):
			add_data_userregistration(id,regNo,firstName,middleName,lastName,gender,contactNo,email,password,regDate,updationDate,passUdateDate)
			st.success("Added ::{} ::To User".format(firstName))


	elif choice == "Read":
		st.subheader("View User Details")
		with st.expander("View"):
			list_of_rgnos = [i[1] for i in view_all_data_userregistration()]
			select_rgno = st.selectbox("Registration Number", list_of_rgnos)
			result = get_user_rgno(select_rgno)
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","regNo","firstName","middleName","lastName","gender","contactNo","email","password","regDate","updationDate","passUdateDate"])
			st.dataframe(clean_df)

		# with st.expander("Task Status"):
		# 	task_df = clean_df['Status'].value_counts().to_frame()
		# 	# st.dataframe(task_df)
		# 	task_df = task_df.reset_index()
		# 	st.dataframe(task_df)

		# 	p1 = px.pie(task_df,names='index',values='Status')
		# 	st.plotly_chart(p1,use_container_width=True)


	elif choice == "Update":
		st.subheader("Edit Details")
		with st.expander("Current Data"):
			result = view_all_data_userregistration()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","regNo","firstName","middleName","lastName","gender","contactNo","email","password","regDate","updationDate","passUdateDate"])
			st.dataframe(clean_df)

		list_of_user_id = [i[0] for i in view_all_data_userregistration()]
		selected_user_id = st.selectbox("id",list_of_user_id)
		user_id_result = get_user_id(selected_user_id)
		# st.write(user_id_result)

		if user_id_result:
			id = user_id_result[0][0]
			regNo = user_id_result[0][1]
			firstName = user_id_result[0][2]
			middleName=user_id_result[0][3]
			lastName=user_id_result[0][4]
			gender=user_id_result[0][5]
			contactNo=user_id_result[0][6]
			email=user_id_result[0][7]
			password=user_id_result[0][8]
			regDate=user_id_result[0][9]
			updationDate=user_id_result[0][10]
			passUdateDate=user_id_result[0][11]


			col1,col2 = st.columns(2)
			
			with col1:
				new_user_id = st.text_input("user id",id)

			with col2:
				new_regNo = st.selectbox("Registration Number",list_of_regno)
				new_firstName = st.text_input("First Name",firstName)
				new_middleName=st.text_input("Middle Name",middleName)
				new_lastName=st.text_input("Last Name",lastName)
				new_gender=st.selectbox("Gender",list_of_gender)
				new_contactNo=st.text_input("Contact Number",contactNo)
				new_email=st.text_input("Email",email)
				new_password=st.text_input("Password",password)
				new_regDate=st.text_input("Registration Date",regDate)
				new_updationDate=st.text_input("Updation Date",updationDate)
				new_passUdateDate=st.text_input("Pass issued date",passUdateDate)

			if st.button("Update"):
				edit_user_data(new_user_id,new_regNo,new_firstName,new_middleName,new_lastName,new_gender,new_contactNo,new_email,new_password,new_regDate,new_updationDate,new_passUdateDate,id,regNo,firstName,middleName,lastName,gender,contactNo,email,password,regDate,updationDate,passUdateDate)
				st.success("Updated ::{} ::To {}".format(id,new_user_id))

			with st.expander("View Updated Data"):
				result = view_all_data_userregistration()
				# st.write(result)
				clean_df = pd.DataFrame(result,columns=["id","regNo","firstName","middleName","lastName","gender","contactNo","email","password","regDate","updationDate","passUdateDate"])
				st.dataframe(clean_df)


	elif choice == "Delete":
		st.subheader("Delete")
		with st.expander("View Data"):
			result = view_all_data_userregistration()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","regNo","firstName","middleName","lastName","gender","contactNo","email","password","regDate","updationDate","passUdateDate"])
			st.dataframe(clean_df)

		unique_list = [i[0] for i in view_all_data_userregistration()]
		delete_by_user_id =  st.selectbox("Select user",unique_list)
		if st.button("Delete"):
			delete_data(delete_by_user_id)
			st.warning("Deleted: '{}'".format(delete_by_user_id))

		with st.expander("Updated Data"):
			result = view_all_data_userregistration()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","regNo","firstName","middleName","lastName","gender","contactNo","email","password","regDate","updationDate","passUdateDate"])
			st.dataframe(clean_df)

	else:
		st.subheader("About ToDo List App")
		st.info("Built with Streamlit")
		st.info("Jesus Saves @JCharisTech")
		st.text("Jesse E.Agbe(JCharis)")


if __name__ == '__main__':
	main()

