import streamlit as st
import pandas as pd
from db_fxns import *
from userlog import *
from register import register

import streamlit.components.v1 as stc


HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <p style="color:white;text-align:center;">HOSTEL REGISTRATION</p>
    </div>
    """


def registration():
	stc.html(HTML_BANNER)

	menu = ["Read"]
	choice = st.sidebar.selectbox("Menu", menu)
	create_table_registration()

	if choice == "Create":
		st.subheader("Add Item")
		col1,col2 = st.beta_columns(2)
		
		with col1:
			id = st.text_input("User ID")
			roomno=st.text_input("Room Number")
			seater=st.text_input("Sharing")
			feespm=st.text_input("Fees per month")
			foodstatus=st.text_input("Food Availability")
			stayfrom=st.date_input("Stay From")
			duration=st.text_input("Duration")
			course=st.text_input("Course")
			regno=st.text_input("Registration Number")
			firstName=st.text_input("First Name")
			middleName=st.text_input("Middle Name")
			lastName=st.text_input("Last Name")
			gender=st.text_input("Gender")
			contactno=st.text_input("Contact Number")
			emailid=st.text_input("Email address")
			egycontactno=st.text_input("Emergency Contact Number")
			guardianName=st.text_input("Guardian Name")
			guardianRelation=st.text_input("Guardian Relation")
			guardianContactno=st.text_input("Guardian Contact Number")
			corresAddress=st.text_input("Correspondence Address")
			corresCIty=st.text_input("Correspondence City")
			corresState=st.text_input("Correspondence State")
			corresPincode=st.text_input("Correspondence Pincode")
			pmntAddress=st.text_input("Permanent Address")
			pmntCity=st.text_input("Permanent City")
			pmnatetState=st.text_input("Permanent State")
			pmntPincode=st.text_input("Permanent Pincode")
			postingDate=st.date_input("Posting Date")
			updationDate=st.date_input("Updation Date")

            

 
        
           
		
		
# course_id,course_name,course_format,singer_name,movie_name,movie_name,course_image,audio_file
		
			

		

		if st.button("submit"):
			add_data_registration(id,roomno,seater,feespm,foodstatus,stayfrom,duration,course,regno,firstName,middleName,lastName,gender,contactno,emailid,egycontactno,guardianName,guardianRelation,guardianContactno,corresAddress,corresCIty,corresState,corresPincode,pmntAddress,pmntCity,pmnatetState,pmntPincode,postingDate,updationDate)
			st.success("Added ::{} ::To Registration ID".format(id))


	elif choice == "Read":
		st.subheader("My Profile")
		with st.expander("View"):
			result = get_registration_detail(emailid)
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","roomno","seater","feespm","foodstatus","stayfrom","duration","course","regno","firstName","middleName","lastName","gender","contactno","emailid","egycontactno","guardianName","guardianRelation","guardianContactno","corresAddress","corresCIty","corresState","corresPincode","pmntAddress","pmntCity","pmnatetState","pmntPincode","postingDate","updationDate"])
			st.dataframe(clean_df)

	# 	# with st.expander("Task Status"):
	# 	# 	task_df = clean_df['Status'].value_counts().to_frame()
	# 	# 	# st.dataframe(task_df)
	# 	# 	task_df = task_df.reset_index()
	# 	# 	st.dataframe(task_df)

	# 	# 	p1 = px.pie(task_df,names='index',values='Status')
	# 	# 	st.plotly_chart(p1,use_container_width=True)


	elif choice == "Update":
		st.subheader("Update Profile")
		with st.expander("Current Data"):
			result = view_all_data_registration()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","roomno","seater","feespm","foodstatus","stayfrom","duration","course","regno","firstName","middleName","lastName","gender","contactno","emailid","egycontactno","guardianName","guardianRelation","guardianContactno","corresAddress","corresCIty","corresState","corresPincode","pmntAddress","pmntCity","pmnatetState","pmntPincode","postingDate","updationDate"])
			st.dataframe(clean_df)

		list_of_registration_id = [i[0] for i in view_all_registration()]
		selected_registration_id = st.selectbox("id",list_of_registration_id)
		registration_id_result = get_registration_id(selected_registration_id)
		# st.write(user_id_result)

		if registration_id_result:
			id = registration_id_result[0][0]
			roomno=registration_id_result[0][1]
			seater=registration_id_result[0][2]
			feespm=registration_id_result[0][3]
			foodstatus=registration_id_result[0][4]
			stayfrom=registration_id_result[0][5]
			duration=registration_id_result[0][6]
			course=registration_id_result[0][7]
			regno=registration_id_result[0][8]
			firstName=registration_id_result[0][9]
			middleName=registration_id_result[0][10]
			lastName=registration_id_result[0][11]
			gender=registration_id_result[0][12]
			contactno=registration_id_result[0][13]
			emailid=registration_id_result[0][14]
			egycontactno=registration_id_result[0][15]
			guardianName=registration_id_result[0][16]
			guardianRelation=registration_id_result[0][17]
			guardianContactno=registration_id_result[0][18]
			corresAddress=registration_id_result[0][19]
			corresCIty=registration_id_result[0][20]
			corresState=registration_id_result[0][21]
			corresPincode=registration_id_result[0][22]
			pmntAddress=registration_id_result[0][23]
			pmntCity=registration_id_result[0][24]
			pmnatetState=registration_id_result[0][25]
			pmntPincode=registration_id_result[0][26]
			postingDate=registration_id_result[0][27]
			updationDate=registration_id_result[0][28]


			col1,col2 = st.columns(2)
			
			with col1:
				new_id = st.number_input("registration id",id)

			with col2:
				new_roomno=st.text_input("Room Number",roomno)
				new_seater=st.text_input("Sharing",seater)
				new_feespm=st.text_input("Fees per month",feespm)
				new_foodstatus=st.text_input("Food Availability",foodstatus)
				new_stayfrom=st.date_input("Stay From",stayfrom)
				new_duration=st.text_input("Duration",duration)
				new_course=st.text_input("Course",course)
				new_regno=st.text_input("Registration Number",regno)
				new_firstName=st.text_input("First Name",firstName)
				new_middleName=st.text_input("Middle Name",middleName)
				new_lastName=st.text_input("Last Name",lastName)
				new_gender=st.text_input("Gender",gender)
				new_contactno=st.text_input("Contact Number",contactno)
				new_emailid=st.text_input("Email address",emailid)
				new_egycontactno=st.text_input("Emergency Contact Number",egycontactno)
				new_guardianName=st.text_input("Guardian Name",guardianName)
				new_guardianRelation=st.text_input("Guardian Relation",guardianRelation)
				new_guardianContactno=st.text_input("Guardian Contact Number",guardianContactno)
				new_corresAddress=st.text_input("Correspondence Address",corresAddress)
				new_corresCIty=st.text_input("Correspondence City",corresCIty)
				new_corresState=st.text_input("Correspondence State",corresState)
				new_corresPincode=st.text_input("Correspondence Pincode",corresPincode)
				new_pmntAddress=st.text_input("Permanent Address",pmntAddress)
				new_pmntCity=st.text_input("Permanent City",pmntCity)
				new_pmnatetState=st.text_input("Permanent State",pmnatetState)
				new_pmntPincode=st.text_input("Permanent Pincode",pmntPincode)
				new_postingDate=st.date_input("Posting Date",postingDate)
				new_updationDate=updationDate
			
			if st.button("Update Task"):
				edit_registraion_data(new_id,new_roomno,new_seater,new_feespm,new_foodstatus,new_stayfrom,new_duration,new_course,new_regno,new_firstName,new_middleName,new_lastName,new_gender,new_contactno,new_emailid,new_egycontactno,new_guardianName,new_guardianRelation,new_guardianContactno,new_corresAddress,new_corresCIty,new_corresState,new_corresPincode,new_pmntAddress,new_pmntCity,new_pmnatetState,new_pmntPincode,new_postingDate,new_updationDate,id,roomno,seater,feespm,foodstatus,stayfrom,duration,course,regno,firstName,middleName,lastName,gender,contactno,emailid,egycontactno,guardianName,guardianRelation,guardianContactno,corresAddress,corresCIty,corresState,corresPincode,pmntAddress,pmntCity,pmnatetState,pmntPincode,postingDate,updationDate)
				st.success("Updated ::{} ::To {}".format(id,new_id))

			with st.expander("View Updated Data"):
				result = view_all_data_registration()
				# st.write(result)
				clean_df = pd.DataFrame(result,columns=["id","roomno","seater","feespm","foodstatus","stayfrom","duration","course","regno","firstName","middleName","lastName","gender","contactno","emailid","egycontactno","guardianName","guardianRelation","guardianContactno","corresAddress","corresCIty","corresState","corresPincode","pmntAddress","pmntCity","pmnatetState","pmntPincode","postingDate","updationDate"])
				st.dataframe(clean_df)


	elif choice == "Delete":
		st.subheader("Delete")
		with st.expander("View Data"):
			result = view_all_data_registration()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","roomno","seater","feespm","foodstatus","stayfrom","duration","course","regno","firstName","middleName","lastName","gender","contactno","emailid","egycontactno","guardianName","guardianRelation","guardianContactno","corresAddress","corresCIty","corresState","corresPincode","pmntAddress","pmntCity","pmnatetState","pmntPincode","postingDate","updationDate"])
			st.dataframe(clean_df)

		unique_list = [i[0] for i in view_all_registration()]
		delete_by_registration_id =  st.selectbox("Select registration",unique_list)
		if st.button("Delete"):
			delete_registration_data(delete_by_registration_id)
			st.warning("Deleted: '{}'".format(delete_by_registration_id))

		with st.expander("Updated Data"):
			result = view_all_data_registration()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","roomno","seater","feespm","foodstatus","stayfrom","duration","course","regno","firstName","middleName","lastName","gender","contactno","emailid","egycontactno","guardianName","guardianRelation","guardianContactno","corresAddress","corresCIty","corresState","corresPincode","pmntAddress","pmntCity","pmnatetState","pmntPincode","postingDate","updationDate"])
			st.dataframe(clean_df)

	# else:
	# 	st.subheader("About ToDo List App")
	# 	st.info("Built with Streamlit")
	# 	st.info("Jesus Saves @JCharisTech")
	# 	st.text("Jesse E.Agbe(JCharis)")


if __name__ == '__main__':
	main()

