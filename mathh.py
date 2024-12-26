import re
import pandas
from datetime import datetime


def specialCharacterCheck(field,value):
    if not value.replace(" ","").isalpha():
        print(f"Error: {field} should only contain alphabets.")
        return True
def mobileNumberCheck(mobile_number):
    if not re.match(r'^\+91[1-9]{1}[0-9]{9}$', mobile_number):
        print("Error: Mobile number must be exactly 10 digits and cannot start with 0.")
        return True
    return mobile_number
def dateConversion(date_of_birth):
    try:
        date_of_birth = datetime.strptime(date_of_birth, '%d-%m-%Y').date()
        return date_of_birth
    except ValueError:
        print("Error: Date of birth should be in dd-mm-yyyy format.")
        return True
def addressLength(address):
    if(len(address)<20):
        print("Address must have more than 20 characters")
        return True
def selectQuery(table_name,field_name,field_value,cursor,extra_field_name=1, extra_field_value=1):
    sql=f'Select 1 from {table_name} where {field_name} = %s and {extra_field_name}=%s'
    try:
        cursor.execute(sql,(field_value,extra_field_value))
        result=cursor.fetchone()
        if result[0]!=1:
            pass
    except Exception as e:
       print(f"Entered {field_name} do not exist")
       return True
    
def displayName(sql,cursor):
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
