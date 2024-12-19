from validation import authenticate_user
from connection import conn
from student import *

def display_menu():
    print("Menu:")
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
    print("0. Exit")
    choice= input("Enter the function you would like to perform in menu: ")
    return choice
def main():
    if not authenticate_user():
        print("Authentication failed , User credentials are invalid! 😞")
        return
    
    print("Authentication successfull 😄")
    cursor = conn.cursor()

    while True:
        choice=display_menu()
        if choice== '0':
            exit
        elif choice == '1':
            name = input('enter new student name: ')
            gender = input('Male/Female: ')
            fathers_name = input('enter guardian name: ')
            address = input('enter address: ')
            date_of_birth = input('enter DOB: ')
            mobile_number = "+91" + input('enter mobile number: ')
            course_name = input('enter course details: ')
            Year = input('enter year of admission: ')
            add_student(name, gender, fathers_name, address, date_of_birth, mobile_number, course_name,Year)


if __name__ == "__main__":
    main()