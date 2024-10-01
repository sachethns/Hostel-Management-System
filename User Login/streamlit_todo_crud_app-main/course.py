import streamlit as st
import pandas as pd
from db_fxns import *

import streamlit.components.v1 as stc


HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <p style="color:white;text-align:center;">COURSE DETAILS</p>
    </div>
    """


def courses():
	stc.html(HTML_BANNER)

	menu = ["Read"]
	choice = st.sidebar.selectbox("Menu", menu)
	create_table_courses()

	if choice == "Create":
		st.subheader("Add Item")
		col1,col2 = st.beta_columns(2)
		
		with col1:
			id = st.number_input("Course ID")
			course_code=st.text_input("Course Code")
			course_sn=st.text_input("Course Short Name")
			course_fn=st.text_input("Course Full name")
			posting_date=st.date_input("Posting Date")

 
        
           
		
		
# course_id,course_name,course_format,singer_name,movie_name,movie_name,course_image,audio_file
		
			

		

		if st.button("submit"):
			add_data_courses(id,course_code,course_sn,course_fn,posting_date)
			st.success("Added ::{} ::To Courses".format(id))


	elif choice == "Read":
		st.subheader("View Items")
		with st.beta_expander("View All"):
			result = view_all_data_courses()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","course_code","course_sn","course_fn","posting_date"])
			st.dataframe(clean_df)

	# 	# with st.beta_expander("Task Status"):
	# 	# 	task_df = clean_df['Status'].value_counts().to_frame()
	# 	# 	# st.dataframe(task_df)
	# 	# 	task_df = task_df.reset_index()
	# 	# 	st.dataframe(task_df)

	# 	# 	p1 = px.pie(task_df,names='index',values='Status')
	# 	# 	st.plotly_chart(p1,use_container_width=True)


	elif choice == "Update":
		st.subheader("Edit Items")
		with st.beta_expander("Current Data"):
			result = view_all_data_courses()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","course_code","course_sn","course_fn","posting_date"])
			st.dataframe(clean_df)

		list_of_course_id = [i[0] for i in view_all_courses()]
		selected_course_id = st.selectbox("id",list_of_course_id)
		course_id_result = get_course_id(selected_course_id)
		# st.write(user_id_result)

		if course_id_result:
			id = course_id_result[0][0]
			course_code = course_id_result[0][1]
			course_sn = course_id_result[0][2]
			course_fn=course_id_result[0][3]
			posting_date=course_id_result[0][4]

			col1,col2 = st.columns(2)
			
			with col1:
				new_course_id = st.number_input("Course id",id)

			with col2:
				new_course_code = st.text_input("course_code",course_code)
				new_course_sn=st.text_input("course_sn",course_sn)
				new_course_fn=st.text_input("course_fn",course_fn)
				new_posting_date=st.date_input("posting_date",posting_date)

			if st.button("Update Task"):
				edit_course_data(new_course_id,new_course_code,new_course_sn,new_course_fn,new_posting_date,id,course_code,course_sn,course_fn,posting_date)
				st.success("Updated ::{} ::To {}".format(id,new_course_id))

			with st.beta_expander("View Updated Data"):
				result = view_all_data_courses()
				# st.write(result)
				clean_df = pd.DataFrame(result,columns=["id","course_code","course_sn","course_fn","posting_date"])
				st.dataframe(clean_df)


	elif choice == "Delete":
		st.subheader("Delete")
		with st.beta_expander("View Data"):
			result = view_all_data_courses()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","course_code","course_sn","course_fn","posting_date"])
			st.dataframe(clean_df)

		unique_list = [i[0] for i in view_all_courses()]
		delete_by_course_id =  st.selectbox("Select course",unique_list)
		if st.button("Delete"):
			delete_course_data(delete_by_course_id)
			st.warning("Deleted: '{}'".format(delete_by_course_id))

		with st.beta_expander("Updated Data"):
			result = view_all_data_courses()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["id","course_code","course_sn","course_fn","posting_date"])
			st.dataframe(clean_df)

	# else:
	# 	st.subheader("About ToDo List App")
	# 	st.info("Built with Streamlit")
	# 	st.info("Jesus Saves @JCharisTech")
	# 	st.text("Jesse E.Agbe(JCharis)")


if __name__ == '__main__':
	main()

