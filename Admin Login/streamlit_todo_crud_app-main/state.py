import streamlit as st
import pandas as pd
from db_fxns import *

import streamlit.components.v1 as stc


HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <p style="color:white;text-align:center;">STATE DETAILS</p>
    </div>
    """


def state():
	stc.html(HTML_BANNER)

	menu = ["Read"]
	choice = st.sidebar.selectbox("Menu", menu)
	create_table_states()
	if choice == "Read":
		st.subheader("View Items")
		with st.expander("View All"):
			result = view_all_data_states()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","State"])
			st.dataframe(clean_df)

	if choice == "Create":
		st.subheader("Add Item")
		col1,col2 = st.columns(2)
		
		with col1:
			id = st.number_input("State ID")
			State=st.text_input("State Name")

 
        
           
		
		
# song_id,singer_id,song_name,song_format,singer_name,singer_name,song_image,audio_file
		
			

		

		if st.button("submit"):
			add_data_states(id,State)
			st.success("Added ::{} ::To state".format(State))



	elif choice == "Update":
		st.subheader("Edit Items")
		with st.expander("Current Data"):
			result = view_all_data_states()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","State"])
			st.dataframe(clean_df)

		list_of_state_id = [i[0] for i in view_all_states()]
		selected_state_id = st.selectbox("id",list_of_state_id)
		id_result = get_state_id(selected_state_id)
		# st.write(user_id_result)

		if id_result:
			id = id_result[0][0]
			State = id_result[0][1]


			col1,col2 = st.columns(2)
			
			with col1:
				new_state_id = st.number_input("state id",id)

			with col2:
				new_state=st.text_input("State Name",State)

			if st.button("Update Task"):
				edit_state_data(new_state_id,new_state,id,State)
				st.success("Updated ::{} ::To {}".format(id))

			with st.expander("View Updated Data"):
				result = view_all_data_states()
				# st.write(result)
				clean_df = pd.DataFrame(result,columns=["id","State"])
				st.dataframe(clean_df)


	elif choice == "Delete":
		st.subheader("Delete")
		with st.expander("View Data"):
			result = view_all_data_states()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","State"])
			st.dataframe(clean_df)

		unique_list = [i[0] for i in view_all_states()]
		delete_by_state_id =  st.selectbox("Select state",unique_list)
		if st.button("Delete"):
			delete_state_data(delete_by_state_id)
			st.warning("Deleted: '{}'".format(delete_by_state_id))

		with st.expander("Updated Data"):
			result = view_all_data_states()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","State"])
			st.dataframe(clean_df)

	# else:
	# 	st.subheader("About ToDo List App")
	# 	st.info("Built with Streamlit")
	# 	st.info("Jesus Saves @JCharisTech")
	# 	st.text("Jesse E.Agbe(JCharis)")


if __name__ == '__main__':
	main()

