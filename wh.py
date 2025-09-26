def show_menu():
    print("Menu\n"
          "1)add user \n"
          "2)login \n"
          "3)exit")
    option = input("Enter your choice: ")
    return option


user_list = []


def get_user():
    user = {"name": input("Enter your name: "),
            "family": input("Enter your family: "),
            "username": input("Enter your username: "),
            "password": input("Enter your password: ")}

    if not is_duplicate():
      user_list.append(user)
      print("user saved")
    else:
        print("user already exists")
    return user
def login():
    user_name = input("Enter your  username: ")
    password = input("Enter your password: ")


    for user in user_list:
        if user["username"] == user_name and user["password"] == password:
            print("welcome")
        else:
            print("wrong username or password")
        return user


def is_duplicate():
    user_name = input("Enter your  username: ")


    for user in user_list:
        if user["username"] == user_name :
         print("duplicate user")
         return True