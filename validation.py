def authenticate_user():
    user_id=input("Enter user ID: ")
    password=input("Enter password: ")

    if user_id == "Harshitha" and password == "root":
        return True
    else:
        return False