def main():
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    dob = input("Enter your date of birth: ")

    file_content = f"User Name: {user_name}\nAge: {user_age}\nDate of Birth: {dob}"

    file_name = "user_info.txt"
    with open(file_name, "w") as file:
        file.write(file_content)

    print(f"User information saved to {file_name}")


main()
