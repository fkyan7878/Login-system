from user import User
from storage import save_users, load_users
from security import hash_password
users = load_users()

while True:
    print("\n--- Login-system ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        hashed_password = hash_password(password)

        new_user = User(username, hashed_password)

        found = False

        for user in users:
          if user["username"] == username:
            print("Username already exists!")
            found = True
            break
        if not found:
          users.append(new_user.to_dict())
          save_users(users)

          print("Register successful!")

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        hashed_password = hash_password(password)

        found = False
        for user in users:
             if user["username"] == username and user["password"] == hashed_password :
                 print("Login successful")
                 found = True
                 while True:
                   print("\n--- Dashboard ---")
                   print("1. Show info")
                   print("2.change password")
                   print("3. Logout")

                   dash_choice = input("Choose: ")

                   if dash_choice == "1":
                     print("Username:", user["username"])
                   elif dash_choice == "2":
                      old_password = input("Enter old password : ")
                      old_password = hash_password(old_password)
                      if user["password"] != old_password :
                        print("password is incorrect")
                      else:
                        new_password = input("Enter new password : ")
                        user["password"] = hash_password(new_password)
                        save_users(users)
                        print("Password changed successfully")
                   elif dash_choice == "3":
                     print("Logged out")
                     break
                 break
             

        if found == False:
            print("Invalid username or password")


    elif choice == "3":
        print("Goodbye!")
        break

