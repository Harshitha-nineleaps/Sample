from connection import conn
from datetime import datetime
from student import *
import pandas

cursor=conn.cursor()

def addTeacher(name, gender, address, mobile_number, course_names,date_of_joining):
    if(specialCharacterCheck("name",name)):return
    date_of_joining=dateConversion(date_of_joining)
    if date_of_joining is True: return
    while(True):
        courses=[]
        counter=0
        for item in course_names.split(','):
            counter+=1
            courses.append(item.strip())
        if counter<2: 
            print("Must have atleast 2 courses")
            course_names=input("Please re-enter courses: ")
            continue
        try:
            sql=f"Select count(*) from Courses where 0 "
            for item in courses:
                sql+=f"or course_name='{item}'"
            cursor.execute(sql)
            result=cursor.fetchone()
            if(result[0]!=counter):
                print("One of the course you have entered doesn't exist ")
                course_names=input("Please re-enter courses: ")
                continue
        except Exception as e:
            print(f"An error occuredd: {e}")
        break
    try:
        courses = ",".join(f'{item}' for item in courses)
        past_course=courses
        sql = "INSERT INTO teacher (name, gender, address, mobile_number, course_name, past_course,date_of_joining) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        values = (name, gender,  address, mobile_number,courses,past_course,date_of_joining)
        cursor.execute(sql,values)
        conn.commit()
        print("Teacher added Successfully")
    except Exception as e:
        print(f"An error occured: {e}")



def teacherDetails():
        sql="Select * from teacher where soft_delete=0"
        displayName(sql,cursor)
    


def teacherFilter(filter_values):

    sql="Select * from teacher where 1 "
    for key , value in filter_values.items():
        if key=="course_name":
            sql+=f"and {key} regexp '{value}'"
        else:
            sql+=f"and {key}='{value}'"
    try:
        cursor.execute(sql)
        result=cursor.fetchall()
        if result:
            headers=[i[0] for i in cursor.description]
            print(pandas.DataFrame(result,columns=headers))
        else:
            print("No records found 🧐")
    except Exception as e:
        print(f'An Exception occured: {e}')

        

def delete_teacher_record(teacher_id):

    try:
        sql=f'Select date_of_joining from teacher where teacher_id={teacher_id}'
        cursor.execute(sql)
        join_date = cursor.fetchone()
        if join_date is None:
            print("Error: Teacher not found.")
            return
        else:
            join_date=join_date[0]

        current_date = datetime.now().date()
        employment_duration = (current_date - join_date).days
        
        if employment_duration < 30:
            print("Error: Teacher cannot be deleted as work duration is less than 1 month.")
            return

        cursor.execute(f"UPDATE teacher SET soft_delete =1 WHERE teacher_id = {teacher_id}")

        conn.commit()
        print("Teacher details deleted successfully")

    except Exception as e:
        print(f"An Error occured: {e}")  



def teacherPastCourse(teacher_id):

    try:
        sql=f"Select past_course , course_name from teacher where teacher_id={teacher_id}"
        cursor.execute(sql)
        result=cursor.fetchone()
        if result[0]!=result[1] :
            print(f"Past course of teacher is {result[0]} , teacher has changed the course")
        else:
            print(f"Past course of teacher is {result[0]} , teacher has not changed the course")
    except:
        print('Given teacher_id do not exist')



def updateTeacherInfo(teacher_id, field , value):

    if selectQuery("teacher","teacher_id",teacher_id,cursor):return

    if field=="mobile_number":
        mobile_number = mobileNumberCheck('+91'+value)
        if(mobile_number is True): return
        value=mobile_number

    if field=="course_name":
        while(True):
            courses=[]
            counter=0
            for item in value.split(','):
                counter+=1
                courses.append(str(item.strip()))
            if counter<2: 
                print("Must have atleast 2 courses")
                value=input("Please re-enter courses: ")
                continue
            try:
                sql=f"Select count(*) from Courses where 0 "
                for item in courses:
                    sql+=f"or course_name='{item}' "
                cursor.execute(sql)
                result=cursor.fetchone()
                if(result[0]!=counter):
                    print("One of the course you have entered doesn't exist ")
                    value=input("Please re-enter courses: ")
                    continue
                break
            except Exception as e:
                print(f"An error occured: {e}")
                break
    try:
        sql=f"Update teacher set {field}='{value}' where teacher_id={teacher_id}"
        cursor.execute(sql)
        conn.commit()
        print("Update Successfull 🙌")
    except Exception as e:
        print(f'An Exception occured: {e}')


def searchTeacherName(teacher_name):
    sql=f"Select * from teacher where name='{teacher_name}' and soft_delete=0"
    displayName(sql,cursor)









