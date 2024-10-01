
import mysql.connector
import streamlit as st


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
	database="hostel"
)
c = mydb.cursor()

def check_admin_password(username,password):
    cursor=mydb.cursor()
    cursor.execute("SELECT password FROM admin WHERE username='{}';".format(username))
    data=1
    for i in cursor:
        data=i
    if(type(data)==int):
        st.error("USER NOT AVAILABLE")
        return False
    else:
        for i in data:
            p=i
        if(p==password):
            return True
        else:
            st.error("Wrong Password")
            return False

def check_user_password(email,password):
    cursor=mydb.cursor()
    cursor.execute("SELECT password FROM userregistration WHERE email='{}';".format(email))
    data=1
    for i in cursor:
        data=i
    if(type(data)==int):
        st.error("USER NOT AVAILABLE")
        return False
    else:
        for i in data:
            p=i
        if(p==password):
            return True
        else:
            st.error("Wrong Password")
            return False


def create_table_admin():
	c.execute('CREATE TABLE IF NOT EXISTS admin(id int(11),username TEXT,email TEXT,password varchar(11),reg_date date,updation_date date)')
def create_table_courses():
	c.execute('CREATE TABLE IF NOT EXISTS courses(id int(11),course_code TEXT,course_sn TEXT,course_fn TEXT,posting_date date)')
def create_table_registration():
	c.execute('CREATE TABLE IF NOT EXISTS registration(id int(11),roomno int(11),seater int(11),feespm int(11),foodstatus int(11),stayfrom date,duration int(11),course TEXT,regno int(11),firstName TEXT,middleName TEXT,lastName TEXT,gender TEXT,contactno int(11),emailid TEXT,egycontactno int(11),guardianName TEXT,guardianRelation TEXT,guardianContactno int(11),corresAddress TEXT,corresCIty TEXT,corresState TEXT,corresPincode int(11),pmntAddress TEXT,pmntCity TEXT,pmnatetState TEXT,pmntPincode int(11),postingDate date,updationDate date)')
def create_table_rooms():
	c.execute('CREATE TABLE IF NOT EXISTS rooms(id int(11),seater int(11),room_no int(11),fees int(11),posting_date date)')
def create_table_states():
	c.execute('CREATE TABLE IF NOT EXISTS states(id int(11),State TEXT)')
def create_table_userlog():
	c.execute('CREATE TABLE IF NOT EXISTS userlog(id int(11),userId int(11),userEmail TEXT,password TEXT,city TEXT,country TEXT,logindate date)')
def create_table_userregistration():
	c.execute('CREATE TABLE IF NOT EXISTS userregistration(id int(11),regNo TEXT,firstName TEXT,middleName TEXT,lastName TEXT,gender TEXT,contactNo int(10),email TEXT,password TEXT,regDate date,updationDate date,passUdateDate date)')
def create_table_registration():
	c.execute('CREATE TABLE IF NOT EXISTS registration(id int(11),roomno int(11),seater int(11),feespm int(11),foodstatus int(11),stayfrom date,duration int(11),course TEXT,regno int(11),firstName TEXT,middleName TEXT,lastName TEXT,gender TEXT,contactno int(10),emailid TEXT,egycontactno int(11),guardianName TEXT,guardianRelation TEXT,guardianContactno int(11),corresAddress TEXT,corresCIty TEXT,corresState TEXT,corresPincode int(11),pmntAddress TEXT,pmntCity TEXT,pmnatetState TEXT,pmntPincode int(11),postingDate date,updationDate date)')


def add_data_admin(id,username,email,password,reg_date,updation_date):
	c.execute('INSERT INTO admin(id,username,email,password,reg_date,updation_date) VALUES (%s,%s,%s,%s,%s,%s)',(id,username,email,password,reg_date,updation_date))
	mydb.commit()
def add_data_courses(id,course_code,course_sn,course_fn,posting_date):
	c.execute('INSERT INTO courses(id,course_code,course_sn,course_fn,posting_date) VALUES (%s,%s,%s,%s,%s)',(id,course_code,course_sn,course_fn,posting_date))
	mydb.commit()
def add_data_registration(id,roomno,seater,feespm,foodstatus,stayfrom,duration,course,regno,firstName,middleName,lastName,gender,contactno,emailid,egycontactno,guardianName,guardianRelation,guardianContactno,corresAddress,corresCIty,corresState,corresPincode,pmntAddress,pmntCity,pmnatetState,pmntPincode,postingDate,updationDate):
	c.execute('INSERT INTO registration(id,roomno,seater,feespm,foodstatus,stayfrom,duration,course,regno,firstName,middleName,lastName,gender,contactno,emailid,egycontactno,guardianName,guardianRelation,guardianContactno,corresAddress,corresCIty,corresState,corresPincode,pmntAddress,pmntCity,pmnatetState,pmntPincode,postingDate,updationDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(id,roomno,seater,feespm,foodstatus,stayfrom,duration,course,regno,firstName,middleName,lastName,gender,contactno,emailid,egycontactno,guardianName,guardianRelation,guardianContactno,corresAddress,corresCIty,corresState,corresPincode,pmntAddress,pmntCity,pmnatetState,pmntPincode,postingDate,updationDate))
	mydb.commit()
def add_data_rooms(id,seater,room_no,fees,posting_date):
	c.execute('INSERT INTO rooms(id,seater,room_no,fees,posting_date) VALUES (%s,%s,%s,%s,%s)',(id,seater,room_no,fees,posting_date))
	mydb.commit()
def add_data_states(id,State):
	c.execute('INSERT INTO states(id,State) VALUES (%s,%s)',(id,State))
	mydb.commit()
def add_data_userlog(id,userId,userEmail,password,city,country,logindate):
	c.execute('INSERT INTO userlog(id,userId,userEmail,password,city,country,logindate) VALUES (%s,%s,%s,%s,%s,%s,%s)',(id,userId,userEmail,password,city,country,logindate))
	mydb.commit()
def add_data_userregistration(id,regNo,firstName,middleName,lastName,gender,contactNo,email,password,regDate,updationDate,passUdateDate):
	c.execute('INSERT INTO userregistration(id,regNo,firstName,middleName,lastName,gender,contactNo,email,password,regDate,updationDate,passUdateDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(id,regNo,firstName,middleName,lastName,gender,contactNo,email,password,regDate,updationDate,passUdateDate))
	mydb.commit()
def add_data_registration(id,roomno,seater,feespm,foodstatus,stayfrom,duration,course,regno,firstName,middleName,lastName,gender,contactno,emailid,egycontactno,guardianName,guardianRelation,guardianContactno,corresAddress,corresCIty,corresState,corresPincode,pmntAddress,pmntCity,pmnatetState,pmntPincode,postingDate,updationDate):
	c.execute('INSERT INTO registration(id,roomno,seater,feespm,foodstatus,stayfrom,duration,course,regno,firstName,middleName,lastName,gender,contactno,emailid,egycontactno,guardianName,guardianRelation,guardianContactno,corresAddress,corresCIty,corresState,corresPincode,pmntAddress,pmntCity,pmnatetState,pmntPincode,postingDate,updationDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(id,roomno,seater,feespm,foodstatus,stayfrom,duration,course,regno,firstName,middleName,lastName,gender,contactno,emailid,egycontactno,guardianName,guardianRelation,guardianContactno,corresAddress,corresCIty,corresState,corresPincode,pmntAddress,pmntCity,pmnatetState,pmntPincode,postingDate,updationDate))
	mydb.commit()

def view_all_data_admin():
	c.execute('SELECT * FROM admin')
	data = c.fetchall()
	return data
def view_all_data_courses():
	c.execute('SELECT * FROM courses')
	data = c.fetchall()
	return data
def view_all_data_registration():
	c.execute('SELECT * FROM registration')
	data = c.fetchall()
	return data
def view_all_data_rooms():
	c.execute('SELECT * FROM rooms')
	data = c.fetchall()
	return data
def view_all_data_states():
	c.execute('SELECT * FROM states')
	data = c.fetchall()
	return data
def view_all_data_userlog():
	c.execute('SELECT * FROM userlog')
	data = c.fetchall()
	return data
def view_all_data_userregistration():
	c.execute('SELECT * FROM userregistration')
	data = c.fetchall()
	return data







def view_all_admin():
	c.execute('SELECT DISTINCT id FROM admin')
	data = c.fetchall()
	return data
def view_all_courses():
	c.execute('SELECT DISTINCT id FROM courses')
	data = c.fetchall()
	return data
def view_all_registration():
	c.execute('SELECT DISTINCT id FROM registration')
	data = c.fetchall()
	return data
def view_all_rooms():
	c.execute('SELECT DISTINCT id FROM rooms')
	data = c.fetchall()
	return data
def view_all_states():
	c.execute('SELECT DISTINCT id FROM states')
	data = c.fetchall()
	return data
def view_all_userlog():
	c.execute('SELECT DISTINCT id FROM userlog')
	data = c.fetchall()
	return data
def view_all_userregistration():
	c.execute('SELECT DISTINCT id FROM userregistration')
	data = c.fetchall()
	return data



def get_state_name(State):
	c.execute('SELECT * FROM states WHERE State="{}"'.format(State))
	data = c.fetchall()
	return data


def get_state_id(id):
	c.execute('SELECT * FROM states WHERE id="{}"'.format(id))
	data = c.fetchall()
	return data

def get_registration_id(id):
	c.execute('SELECT * FROM registration WHERE id="{}"'.format(id))
	data = c.fetchall()
	return data

def get_user_id(id):
	c.execute('SELECT * FROM userregistration WHERE id="{}"'.format(id))
	data = c.fetchall()
	return data

def get_room_id(id):
	c.execute('SELECT * FROM rooms WHERE id="{}"'.format(id))
	data = c.fetchall()
	return data

def get_loggeduser_id(id):
	c.execute('SELECT * FROM userlog WHERE id="{}"'.format(id))
	data = c.fetchall()
	return data

def get_course_id(id):
	c.execute('SELECT * FROM courses WHERE id="{}"'.format(id))
	data = c.fetchall()
	return data

def get_admin_id(id):
	c.execute('SELECT * FROM admin WHERE id="{}"'.format(id))
	data = c.fetchall()
	return data


def edit_user_data(new_user_id,new_regNo,new_firstName,new_middleName,new_lastName,new_gender,new_contactNo,new_email,new_password,new_regDate,new_updationDate,new_passUdateDate,id,regNo,firstName,middleName,lastName,gender,contactNo,email,password,regDate,updationDate,passUdateDate):
	c.execute("UPDATE userregistration SET id =%s,regNo=%s,firstName=%s,middleName=%s,lastName=%s,gender=%s,contactNo=%s,email=%s,password=%s,regDate=%s,updationDate=%s,passUdateDate=%s WHERE id=%s and regNo=%s and firstName=%s and middleName=%s and lastName=%s and gender=%s and contactNo=%s and email=%s and password=%s and regDate=%s and updationDate=%s and passUdateDate=%s ",(new_user_id,new_regNo,new_firstName,new_middleName,new_lastName,new_gender,new_contactNo,new_email,new_password,new_regDate,new_updationDate,new_passUdateDate,id,regNo,firstName,middleName,lastName,gender,contactNo,email,password,regDate,updationDate,passUdateDate))
	mydb.commit()
	# data = c.fetchall()
	# return data

def edit_room_data(new_room_id,new_seater,new_room_no,new_fees,new_posting_date,id,seater,room_no,fees,posting_date):
	c.execute("UPDATE rooms SET id =%s,seater=%s,room_no=%s,fees=%s,posting_date=%s WHERE id=%s and seater=%s and room_no=%s and fees=%s and posting_date=%s ",(new_room_id,new_seater,new_room_no,new_fees,new_posting_date,id,seater,room_no,fees,posting_date))
	mydb.commit()
	# data = c.fetchall()
	# return data
"""
def edit_userlog_data(new_id,new_userId,new_userEmail,new_city,new_country,new_logindate,id,userId,userEmail,city,country,logindate):
	c.execute("UPDATE userlog SET id=%s,userId=%s,userEmail=%s,city=%s,country=%s,logindate=%s WHERE id=%s and userId=%s and userEmail=%s and city=%s and country=%s and logindate=%s  ",(new_id,new_userId,new_userEmail,new_city,new_country,new_logindate,id,userId,userEmail,city,country,logindate))
	mydb.commit()
"""
def edit_course_data(new_course_id,new_course_code,new_course_sn,new_course_fn,new_posting_date,id,course_code,course_sn,course_fn,posting_date):
	c.execute("UPDATE courses SET id =%s,course_code=%s,course_sn=%s,course_fn=%s,posting_date=%s WHERE id=%s and course_code=%s and course_sn=%s and course_fn=%s and posting_date=%s ",(new_course_id,new_course_code,new_course_sn,new_course_fn,new_posting_date,id,course_code,course_sn,course_fn,posting_date))
	mydb.commit()

def edit_admin_data(new_id,new_username,new_email,new_password,new_reg_date,new_updation_date,id,username,email,password,reg_date,updation_date):
	c.execute("UPDATE admin SET id =%s,username=%s,email=%s,password=%s,reg_date=%s,updation_date=%s WHERE id=%s and username=%s and email=%s and password=%s and reg_date=%s and updation_date=%s ",(new_id,new_username,new_email,new_password,new_reg_date,new_updation_date,id,username,email,password,reg_date,updation_date))
	mydb.commit()

def edit_registraion_data(new_id,new_roomno,new_seater,new_feespm,new_foodstatus,new_stayfrom,new_duration,new_course,new_regno,new_firstName,new_middleName,new_lastName,new_gender,new_contactno,new_emailid,new_egycontactno,new_guardianName,new_guardianRelation,new_guardianContactno,new_corresAddress,new_corresCIty,new_corresState,new_corresPincode,new_pmntAddress,new_pmntCity,new_pmnatetState,new_pmntPincode,new_postingDate,new_updationDate,id,roomno,seater,feespm,foodstatus,stayfrom,duration,course,regno,firstName,middleName,lastName,gender,contactno,emailid,egycontactno,guardianName,guardianRelation,guardianContactno,corresAddress,corresCIty,corresState,corresPincode,pmntAddress,pmntCity,pmnatetState,pmntPincode,postingDate,updationDate):
	c.execute("UPDATE registration SET id =%s,roomno=%s,seater=%s,feespm=%s,foodstatus=%s,stayfrom=%s,duration=%s,course=%s,regno=%s,firstName=%s,middleName=%s,lastName=%s,gender=%s,contactno=%s,emailid=%s,egycontactno=%s,guardianName=%s,guardianRelation=%s,guardianContactno=%s,corresAddress=%s,corresCIty=%s,corresState=%s,corresPincode=%s,pmntAddress=%s,pmntCity=%s,pmnatetState=%s,pmntPincode=%s,postingDate=%s,updationDate=%s WHERE id=%s and roomno=%s and seater=%s and feespm=%s and foodstatus=%s and stayfrom=%s and duration=%s and course=%s and regno=%s and firstName=%s and middleName=%s and lastName=%s and gender=%s and contactno=%s and emailid=%s and egycontactno=%s and guardianName=%s and guardianRelation=%s and guardianContactno=%s and corresAddress=%s and corresCIty=%s and corresState=%s and corresPincode=%s and pmntAddress=%s and pmntCity=%s and pmnatetState=%s and pmntPincode=%s and postingDate=%s and updationDate=%s ",(new_id,new_roomno,new_seater,new_feespm,new_foodstatus,new_stayfrom,new_duration,new_course,new_regno,new_firstName,new_middleName,new_lastName,new_gender,new_contactno,new_emailid,new_egycontactno,new_guardianName,new_guardianRelation,new_guardianContactno,new_corresAddress,new_corresCIty,new_corresState,new_corresPincode,new_pmntAddress,new_pmntCity,new_pmnatetState,new_pmntPincode,new_postingDate,new_updationDate,id,roomno,seater,feespm,foodstatus,stayfrom,duration,course,regno,firstName,middleName,lastName,gender,contactno,emailid,egycontactno,guardianName,guardianRelation,guardianContactno,corresAddress,corresCIty,corresState,corresPincode,pmntAddress,pmntCity,pmnatetState,pmntPincode,postingDate,updationDate))
	mydb.commit()

def edit_state_data(new_state_id,new_state,id,State):
	c.execute("UPDATE rooms SET id =%s,State=%s WHERE id=%s and State=%s ",(new_state_id,new_state,id,State))
	mydb.commit()


def delete_data(id):
	c.execute('DELETE FROM userregistration WHERE id="{}"'.format(id))
	mydb.commit()

def delete_room_data(id):
	c.execute('DELETE FROM rooms WHERE id="{}"'.format(id))
	mydb.commit()

def delete_userlog_data(id):
	c.execute('DELETE FROM userlog WHERE id="{}"'.format(id))
	mydb.commit()

def delete_course_data(id):
	c.execute('DELETE FROM courses WHERE id="{}"'.format(id))
	mydb.commit()

def delete_admin_data(id):
	c.execute('DELETE FROM admin WHERE id="{}"'.format(id))
	mydb.commit()

def delete_registration_data(id):
	c.execute('DELETE FROM registration WHERE id="{}"'.format(id))
	mydb.commit()

def delete_state_data(id):
	c.execute('DELETE FROM states WHERE id="{}"'.format(id))
	mydb.commit()

"""
def get_room_id(id):
	c.execute('SELECT * FROM rooms WHERE id="{}"'.format(id))
	data = c.fetchall()
	return data
def get_englishsong_id(song_id):
	c.execute('SELECT * FROM english_albums WHERE song_id="{}"'.format(song_id))
	data = c.fetchall()
	return data
def get_loggeduser_id(id):
	c.execute('SELECT * FROM userlog WHERE id="{}"'.format(id))
	data = c.fetchall()
	return data
def get_hindisong_id(song_id):
	c.execute('SELECT * FROM hindi_albums WHERE song_id="{}"'.format(song_id))
	data = c.fetchall()
	return data

# def get_task_by_status(task_status):
# 	c.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(task_status))
# 	data = c.fetchall()


def edit_room_data(new_course_id,new_course_code,new_course_sn,new_course_fn,new_posting_date,id,course_code,course_sn,course_fn,posting_date):
	c.execute("UPDATE rooms SET id =%s,course_code=%s,course_sn=%s,course_fn=%s,posting_date=%s WHERE id=%s and course_code=%s and course_sn=%s and course_fn=%s and posting_date=%s ",(new_course_id,new_course_code,new_course_sn,new_course_fn,new_posting_date,id,course_code,course_sn,course_fn,posting_date))
	mydb.commit()
	# data = c.fetchall()
	# return data
def edit_song_id_data(new_song_id,new_singer_id,new_song_name,new_song_format,new_singer_name,new_audio_file,song_id,singer_id,song_name,song_format,singer_name,audio_file):
	c.execute("UPDATE upload_albums SET song_id=%s,singer_id=%s,song_name=%s,song_format=%s,singer_name=%s,audio_file=%s WHERE song_id=%s,singer_id=%s,song_name=%s,song_format=%s,singer_name=%s,audio_file=%s ",(new_song_id,new_singer_id,new_song_name,new_song_format,new_singer_name,new_audio_file,song_id,singer_id,song_name,song_format,singer_name,audio_file))
	mydb.commit()
	# data = c.fetchall()
	# return data
def edit_userlog_data(new_id,new_userId,new_userEmail,new_userIp,new_city,new_country,new_loginTime,id,userId,userEmail,userIp,city,country,loginTime):
	c.execute("UPDATE userlog SET id=%s,userId=%s,userEmail=%s,userIp=%s,city=%s,country=%s,loginTime=%s WHERE id=%s and userId=%s and userEmail=%s and userIp=%s and city=%s and country=%s and loginTime=%s  ",(new_id,new_userId,new_userEmail,new_userIp,new_city,new_country,new_loginTime,id,userId,userEmail,userIp,city,country,loginTime))
	mydb.commit()
def edit_kannadasong_id_data(new_song_id,new_song_name,new_song_format,new_singer_name,new_movie_name,new_audio_file,song_id,song_name,song_format,singer_name,movie_name,audio_file):
	c.execute("UPDATE kannada_albums SET song_id=%s,song_name=%s,song_format=%s,singer_name=%s,movie_name=%s,audio_file=%s WHERE song_id=%s,song_name=%s,song_format=%s,singer_name=%s,movie_name=%s,audio_file=%s ",(new_song_id,new_song_name,new_song_format,new_singer_name,new_movie_name,new_audio_file,song_id,song_name,song_format,singer_name,movie_name,audio_file))
	mydb.commit()
def edit_hindisong_id_data(new_song_id,new_song_name,new_song_format,new_singer_name,new_movie_name,new_audio_file,song_id,song_name,song_format,singer_name,movie_name,audio_file):
	c.execute("UPDATE hindi_albums SET song_id=%s,song_name=%s,song_format=%s,singer_name=%s,movie_name=%s,audio_file=%s WHERE song_id=%s,song_name=%s,song_format=%s,singer_name=%s,movie_name=%s,audio_file=%s ",(new_song_id,new_song_name,new_song_format,new_singer_name,new_movie_name,new_audio_file,song_id,song_name,song_format,singer_name,movie_name,audio_file))
	mydb.commit()
	
	

def delete_userlog_data(id):
	c.execute('DELETE FROM userlog WHERE id="{}"'.format(id))
	mydb.commit()
def delete_data_upload(song_id):
	c.execute('DELETE FROM upload_albums WHERE song_id="{}"'.format(song_id))
	mydb.commit()
def delete_data_english(song_id):
	c.execute('DELETE FROM english_albums WHERE song_id="{}"'.format(song_id))
	mydb.commit()
def delete_data_kannada(song_id):
	c.execute('DELETE FROM kannada_albums WHERE song_id="{}"'.format(song_id))
	mydb.commit()
def delete_data_hindi(song_id):
	c.execute('DELETE FROM hindi_albums WHERE song_id="{}"'.format(song_id))
	mydb.commit()
"""