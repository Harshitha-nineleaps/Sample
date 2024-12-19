from connection import conn
from datetime import datetime
import mysql.connector
import re
from student import *

def add_student(name, gender, guardian_name, address, date_of_birth, mobile_number, course_name,Year):
    cursor = conn.cursor()
    if not (name.replace(" ", "").isalpha() and guardian_name.replace(" ", "").isalpha()):
        print("Error: Name and Guardian name should only contain alphabets.")
        return

    # Check if mobile number starts with +91 and is followed by 10 digits
    mobile_number = mobile_number.strip() 
    print(mobile_number)
    if not re.match(r'^\+91\d{10}$', mobile_number):
        print("Error: Mobile number should be exactly 10 digits.")
        return
    
    if(gender.lower() not in ('male','female','other')):
        print("Please Enter any one of given choices in gender")
        return

    # Convert date_of_birth to datetime object
    try:
        date_of_birth = datetime.strptime(date_of_birth, '%d-%m-%Y').date()
    except ValueError:
        print("Error: Date of birth should be in dd-mm-yyyy format.")
        return
    past_course = course_name

    if(len(address)<15):
        print("Address must have more than 15 characters")
        return
    
    sql="Select 1 from Courses where course_name=%s"
    try:
        cursor.execute(sql,(course_name,))
        cursor.fetchone()
    except Exception as e:
       print("Entered Course do not exist")
       return
    
    
    # Insert SQL query
    sql = "INSERT INTO students (name, gender, guardian_name, address, date_of_birth, mobile_number, course_name, year, past_course) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (name, gender, guardian_name, address, date_of_birth, mobile_number, course_name, Year, past_course)

    # Execute SQL query
    try:
        cursor.execute(sql, values)
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    

    print("New student added successfully!")