

import streamlit as st
import sqlite3

# Database Connection
def connect_db():
    return sqlite3.connect("mydb.db")

# Create Table if not exists

def Home():
    st.write("Welcome to home page !!")
def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS students (
                    name TEXT,
                    age INTEGER,
                    roll INTEGER PRIMARY KEY,
                    password TEXT,
                    gender TEXT,
                    branch TEXT
                )''')
    conn.commit()
    conn.close()

# Function to Add Record
def add_record(data): 
    conn = connect_db()
    cur = conn.cursor()
    
    try:
        cur.execute("INSERT INTO students(name, age, roll, password, gender, branch) VALUES (?, ?, ?, ?, ?, ?)", data)
        conn.commit()
        st.success("Successfully Registered!")
    except sqlite3.IntegrityError:
        st.error("User already exists!")
    
    conn.close()

# Function to View Records
def view_records():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    result = cur.fetchall()
    conn.close()
    return result

# Display Table Records
def display_records():
    st.subheader("Registered Users")
    data = view_records()
    if data:
        for row in data:
            st.write(f"**Name:** {row[0]}, **Age:** {row[1]}, **Roll No:** {row[2]}, **Gender:** {row[4]}, **Branch:** {row[5]}")
    else:
        st.write("No records found!")

# Signup Form
def signup():
    st.subheader("Signup Form")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=10, max_value=100, step=1)
    roll = st.number_input("Enter your Roll Number", step=1)
    password = st.text_input("Enter your password", type="password")
    repass = st.text_input("Retype your password", type="password")
    gender = st.radio("Select your Gender", options=["Male", "Female"])
    branch = st.selectbox("Select your Branch", options=["AIML", "CSE", "IOT", "Cybersecurity"])

    if st.button("Submit"):
        if password != repass:
            st.error("Passwords do not match!")
        else:
            add_record((name, age, roll, password, gender, branch))

# Initialize DB
create_table()

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home","Signup", "Display Records"])

# Load selected page
if menu== "Home":
    Home()
elif menu == "Signup":
    signup()
elif menu == "Display Records":
    display_records()

# import streamlit as st
# from streamlit_option_menu import 
# import sqlite3

# def connect_db():
#     con= sqlite3.connect("mydb.db")

# def create_Table():
#     conn= connect_db()
#     cur=conn.cursor()
#     cur.execute('create table if not exist students (name text,age int,roll int,password text,gender text, Branch text')
#     conn.commit()
#     conn.close()
    
    
    

# def addrecord(data): 
#     conn= connect_db()
#     cur= conn.cursor()
    
#     try:
#         cur.execute("insert into students(name,age,roll,password,gender,branch) values (?,?,?,?,?,?) ",data)
#         conn.comit()
#     except sqlite3IntegrityError:
#         st.error("User alredy exists !")
  
#     conn.close()
    
# def view_record():
#     conn= connect_db()
#     cur= conn.cursor()
#     cur.execute("select * from student")
#     result= cur.fetchall()
#     conn.close()
#     return result
    
# def display():
#     data= view_record()
#     st.write(data)
 

# def signup():
#   name= st.text_input("Enter your name ")
#   age= st.number_input("Enter yiur age")
#   roll= st.number_input("Enter yiur rollnumner")
#   password= st.text_input("Enter your password", type="password")
#   repass= st.text_input("retype your password", type="password")
#   gender=st.radio("Enter you gender !", options=["Male","Female"])
#   Branch= st.selectbox("Enter your branch", options=["Aiml","Cse","Iot","cybersecurity"])
#   if st.button("Submit"):
#       if password != repass:
#           # st.write(f"hello {name} and your age is {age}")
#           st.error("your password not match")
#       else:
#            st.write("Succesfully added")
#            addrecord((name,age,roll,password,gender,Branch))
#            # st.success(f"{name},{roll},{password},{Branch}")
#            st.success("done registerd !")
    
    
    
    
# create_Table()
    
# st.title("form for login")
# signup()