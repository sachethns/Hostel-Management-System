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

	list_of_roomno = [i[2] for i in view_all_data_rooms()]
	create_table_rooms()




	st.subheader("View Room Details")
	with st.expander("View"):
		select_room=st.selectbox("Select room number",list_of_roomno)
		result = get_room_number(select_room)
		# st.write(result)
		clean_df = pd.DataFrame(result,columns=["Room Number","Seater","Fees Per Month","Occupied","Vacancy"])
		st.dataframe(clean_df)




	

if __name__ == '__main__':
	main()

