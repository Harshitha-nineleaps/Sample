from validation import authenticate_user
from connection import conn
from student import *
from teacher import *

def display_menu():
    print("Menu:")
    print("0. Exit")
    print("1. Add Student")
    print("2. Update Student Information")
    print("3. View Student Details")
    print("4. List Students")
    print("5. View Student's current course")
    print("6. Delete Student")
    print("7. Add Teacher")
    print("8. Update Teacher Information")
    print("9. View Teacher Details")
    print("10. List Teachers")
    print("11. Delete Teacher Record")
    print("12. View Student's past course")
    print("13. View teacher's past course")
    print("14. Search student by name ")
    print("15. Search teacher by name ")
    print("16. Export Student data to a csv file")
    print("17. Import student data from csv file")
    choice= input("Enter the function you would like to perform in menu: ")
    return choice


def main():
    # if not authenticate_user():
    #     print("Authentication failed , User credentials are invalid! 😞")
    #     return
    
    print("Authentication successfull 😄")
    cursor = conn.cursor()

    while True:
        choice=display_menu()
        if choice== '0':
            break
        elif choice == '1':
            name = input('Enter new student name: ')
            gender = input('Male/Female/Other: ')
            guardian_name = input('enter guardian name: ')
            address = input('enter address: ')
            date_of_birth = input('enter DOB: ')
            mobile_number = "+91" + input('enter mobile number: ')
            course_name = input('Enter course details: ')
            Year = input('Enter the year of study (e.g., 1 for first year, 2 for second year, etc.):')
            add_student(name.strip(), gender.strip(), guardian_name.strip(), address.strip(), date_of_birth.strip(), mobile_number.strip(), course_name.strip(),Year.strip())

        elif choice == '2':
            student_id = input('Enter student ID: ')
            while True:
                field = input("Enter the field you would like to update: ")
                if field.strip() not in ('guardian_name', 'address','date_of_birth', 'mobile_number', 'course_name'):
                    print("😨Caution field name should be anyone of these ('guardian_name', 'address','date_of_birth', 'mobile_number', 'course_name')")
                else:
                    value = input(f"Enter new value for {field}: ")
                    update_student_info(student_id, field , value.strip() )
                    break
        
        elif choice == '3':
            studentDetails()

        elif choice == '4' :
            flag=0
            while True:
                field=input(f'''
Enter the field based on which you would like to filter ,
If you like to filter based on more than 1 field please enter those fields separated by coma: ''').split(',')
                valid_fields=['gender','course_name','year']
                for item in field :
                    if item.strip() not in valid_fields:
                        print(f'''
🙎Only following field's can be filtered ('gender','year','course_name') ,
        ----So please enter only these fields----''')
                        break
                else:
                    filter_values={}
                    field = [f.strip() for f in field]
                    if "course_name" in field:
                        filter_values["course_name"]=input("Enter the course_name: ").strip()
                    if "year" in field:
                        filter_values["year"]=input("Enter the year: ").strip()
                    if "gender" in field:
                        filter_values["gender"]=input("Enter the gender: ").strip()
                        
                    studentFilter(filter_values)
                    flag=1
                    break
                if flag==1:
                    break

        
        elif choice=='5':
            student_id=input("Enter the student id: ")
            currentCourse(student_id.strip())


        elif choice=='6':
            student_id=input("Enter the student id: ")
            softDelete(student_id.strip())

        elif choice=='12':
            student_id=input("Enter the student id: ")
            pastCourse(student_id.strip())

                        
        elif choice=='7':
            name = input('Enter new teacher name: ')
            gender = input('Male/Female/Other: ')
            address = input('Enter address: ')
            mobile_number = "+91" + input('enter mobile number: ')
            course_names = input('Provide 2 or more course names separated by coma: ')
            date_of_joining = input('Enter the date of joining: ')
            addTeacher(name.strip(), gender.strip(), address.strip(), mobile_number.strip(), course_names.strip(),date_of_joining.strip())

            
        elif choice=='9':
            teacherDetails()

        elif choice=='10':
            flag=0
            while True:
                field=input(f'''
Enter the field based on which you would like to filter ,
If you like to filter based on more than 1 field please enter those fields separated by coma: ''').split(',')
                valid_fields=['gender','course_name']
                # fields = [f.strip() for f in field.split(',') if f.strip() in valid_fields]
                # print(fields)
                for item in field :
                    if item.strip() not in valid_fields:
                        print(f'''
🙎Only following field's can be filtered ('gender','course_name') ,
        ----So please enter only these fields----''')
                        break
                else:
                    filter_values={}
                    field = [f.strip() for f in field]
                    if "course_name" in field:
                        filter_values["course_name"]=input("Enter the course_name: ").strip()
                    if "gender" in field:
                        filter_values["gender"]=input("Enter the gender: ").strip()
                    teacherFilter(filter_values)
                    flag=1
                    break
                if flag==1:
                    break


        elif choice=='11':
            teacher_id=input("Enter teacher_id: ").strip()
            delete_teacher_record(teacher_id)

        elif choice=='13':
            teacher_id=input("Enter teacher_id: ").strip()
            teacherPastCourse(teacher_id)

        elif choice=='8':
            teacher_id = input('Enter teacher id: ').strip()
            while True:
                field = input("Enter the field you would like to update: ")
                if field.strip() not in ( 'address','mobile_number', 'course_name'):
                    print("😨Caution field name should be anyone of these ('address','mobile_number', 'course_name')")
                    continue
                value = input(f"Enter new value for {field}: ")
                updateTeacherInfo(teacher_id, field , value.strip() )
                break

        elif choice=='14':
            student_name=input("Enter Student name: ")
            searchStudentName(student_name.strip())

        elif choice=='15':
            teacher_name=input("Enter teacher name: ")
            searchTeacherName(teacher_name.strip())

        elif choice=='16':
            exportToCsv()

        elif choice=='17':
            importfromCsv()

        
        
    




                              


if __name__ == "__main__":
    main()