from connection import conn
from datetime import datetime
import pandas
import csv
from mathh import *

cursor=conn.cursor()
        
def add_student(name, gender, guardian_name, address, date_of_birth, mobile_number, course_name,Year):

    if(specialCharacterCheck("name",name)): return
    if(specialCharacterCheck("guardian_name",guardian_name)): return
    if(mobileNumberCheck(mobile_number) is True):return
    
    if(gender.lower() not in ('male','female','other')):
        print("Please Enter any one of given choices in gender")
        return
    
    date_of_birth=dateConversion(date_of_birth)
    if date_of_birth is True: return

    if(addressLength(address)):return

    if(selectQuery("Courses","course_name",course_name,cursor)):return
        
    past_course = course_name

    # Insert SQL query
    sql = "INSERT INTO students (name, gender, guardian_name, address, date_of_birth, mobile_number, course_name, year, past_course) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (name, gender, guardian_name, address, date_of_birth, mobile_number, course_name, Year, past_course)

    # Execute SQL query
    try:
        cursor.execute(sql, values)
        conn.commit()
        print("New student added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    



def update_student_info(student_id, field , value):
    
    if (field=="guardian_name"):
        if specialCharacterCheck("guardian_name",value):return
    
    if(field=="date_of_birth"):
        value=dateConversion(value)
        if value is True: return

    if field=="mobile_number":
        mobile_number = mobileNumberCheck('+91'+value)
        if(mobile_number is True): return
        value=mobile_number

    if field=="address":
        if(addressLength(value)):return

    if field=="course_name":
        sql=f'Select year , past_course ,{field} from students where student_id={student_id}'
        cursor.execute(sql)
        result=cursor.fetchone()
        if(result[0]!=1):
            print('Oops Student is not from 1st year , change in course option is not available 😫')
            return
        else:
            if result[2]==value : 
                print('You have entered the same course_name 🤷') 
                return
            if result[1]!=result[2]:
                print("U have already changed course once , you can not change it again..🚫")
                return
            if(selectQuery("Courses","course_name",value,cursor)):return
            

    try:
        sql=f"Update students set {field}='{value}' where student_id={student_id}"
        cursor.execute(sql)
        conn.commit()
        print("Update Successfull 🙌")
    except Exception as e:
        print(f'An Exception occured: {e}')



def studentDetails():
    sql=f"Select * from students where soft_delete=0"
    displayName(sql,cursor)
       
        
def studentFilter(filter_values):

    try:
        sql="Select * from students where 1 "
        for key,value in filter_values.items():
            sql+=f"and {key}='{value}'"
        cursor.execute(sql)
        result=cursor.fetchall()
        if result:
            headers=[i[0] for i in cursor.description]
            print(pandas.DataFrame(result,columns=headers))
        else:
            print("No records found 🧐")
    except Exception as e:
        print(f'An Exception occured: {e}')


def currentCourse(student_id):

    try:
        sql=f"Select course_name from students where student_id={student_id}"
        cursor.execute(sql)
        result=cursor.fetchone()
        print(f"{result[0]} is the current course of Student")
    except:
        print('Given student_id do not exist')


def softDelete(student_id):
    try:
        if(selectQuery("students","student_id",student_id,cursor,"soft_delete",0)):return
        sql=f"Update students set soft_delete=true where student_id={student_id}"
        print(sql)
        cursor.execute(sql)
        conn.commit()
        print("Deletion successfull 🤖")
    except Exception as e:
        print(f'An error occured {e}')

    

def pastCourse(student_id):

    try:
        sql=f"Select past_course , course_name from students where student_id={student_id}"
        cursor.execute(sql)
        result=cursor.fetchone()
        if result[0]!=result[1] :
            print(f"Past course of student is {result[0]} , Student has changed the course")
        else:
            print(f"Past course of student is {result[0]} , Student has not changed the course")
    except:
        print('Given student_id do not exist')


def searchStudentName(student_name):

    sql=f"Select * from students where name='{student_name}'"
    displayName(sql,cursor)
    

def exportToCsv():
    try:
        sql="Select * from students"
        cursor.execute(sql)
        rows=cursor.fetchall()
        column_headers=[i[0] for i in cursor.description]
        with open('student_data.csv', mode='w') as file:
            for row in rows:
                writer = csv.writer(file)
                writer.writerow(column_headers)  
                writer.writerow(row)
        print("Data has been exported to 'student_data.csv' successfully.")

    except Exception as e:
        print(f"An error occured:{e}")


def importfromCsv():
    try:
        with open('student_data.csv', mode='r') as file:
            reader = csv.reader(file)   
            for row in reader:
                print(row)
    except Exception as e:
        print(f"An error occured: {e}")













    

 


