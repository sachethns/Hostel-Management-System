import streamlit as st
import pandas as pd
from db_fxns import *

import streamlit.components.v1 as stc


HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <p style="color:white;text-align:center;">ROOM DETAILS</p>
    </div>
    """


def room():
	stc.html(HTML_BANNER)

	menu = ["Create", "Read", "Update", "Delete"]
	choice = st.sidebar.selectbox("Menu", menu)
	create_table_rooms()

	if choice == "Create":
		st.subheader("Add room")
		col1,col2 = st.columns(2)
		
		with col1:
			id = st.text_input("Room id")
			seater=st.text_input("Seater")
			room_no=st.text_input("Room Number")
			fees=st.text_input("Fees")
			posting_date=st.date_input("Posting Date")

 
        
           
		
		
# song_id,song_name,song_format,singer_name,movie_name,movie_name,song_image,audio_file
		
			

		

		if st.button("Submit"):
			add_data_rooms(id,seater,room_no,fees,posting_date)
			st.success("Added ::{} ::To Room ID".format(id))


	elif choice == "Read":
		st.subheader("View rooms")
		with st.expander("View All"):
			result = view_all_data_rooms()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","seater","room_no","fees","posting_date"])
			st.dataframe(clean_df)

	# 	# with st.expander("Task Status"):
	# 	# 	task_df = clean_df['Status'].value_counts().to_frame()
	# 	# 	# st.dataframe(task_df)
	# 	# 	task_df = task_df.reset_index()
	# 	# 	st.dataframe(task_df)

	# 	# 	p1 = px.pie(task_df,names='index',values='Status')
	# 	# 	st.plotly_chart(p1,use_container_width=True)


	elif choice == "Update":
		st.subheader("Edit rooms")
		with st.expander("Current Data"):
			result = view_all_data_rooms()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","seater","room_no","fees","posting_date"])
			st.dataframe(clean_df)

		list_of_room_id = [i[0] for i in view_all_rooms()]
		selected_room_id = st.selectbox("id",list_of_room_id)
		room_id_result = get_room_id(selected_room_id)
		# st.write(user_id_result)

		if room_id_result:
			id = room_id_result[0][0]
			seater = room_id_result[0][1]
			room_no = room_id_result[0][2]
			fees=room_id_result[0][3]
			posting_date=room_id_result[0][4]

			col1,col2 = st.columns(2)
			
			with col1:
				new_room_id = st.text_input("Room id",id)

			with col2:
				new_seater = st.text_input("Seater",seater)
				new_room_no=st.text_input("Room Number",room_no)
				new_fees=st.text_input("Fees",fees)
				new_posting_date=st.date_input("Posting Date",posting_date)

			if st.button("Update"):
				edit_room_data(new_room_id,new_seater,new_room_no,new_fees,new_posting_date,id,seater,room_no,fees,posting_date)
				st.success("Updated ::{} ::To {}".format(id,new_room_id))

			with st.expander("View Updated Data"):
				result = view_all_data_rooms()
				# st.write(result)
				clean_df = pd.DataFrame(result,columns=["id","seater","room_no","fees","posting_date"])
				st.dataframe(clean_df)


	elif choice == "Delete":
		st.subheader("Delete")
		with st.expander("View Data"):
			result = view_all_data_rooms()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","seater","room_no","fees","posting_date"])
			st.dataframe(clean_df)

		unique_list = [i[0] for i in view_all_data_rooms()]
		delete_by_room_id =  st.selectbox("Select Room",unique_list)
		if st.button("Delete"):
			delete_room_data(delete_by_room_id)
			st.warning("Deleted: '{}'".format(delete_by_room_id))

		with st.expander("Updated Data"):
			result = view_all_data_rooms()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","seater","room_no","fees","posting_date"])
			st.dataframe(clean_df)

	# else:
	# 	st.subheader("About ToDo List App")
	# 	st.info("Built with Streamlit")
	# 	st.info("Jesus Saves @JCharisTech")
	# 	st.text("Jesse E.Agbe(JCharis)")


if __name__ == '__main__':
	main()

