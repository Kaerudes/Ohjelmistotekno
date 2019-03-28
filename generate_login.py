import login


def main():
    print("Enter your firstname:")
    firstname = input()
    print("Enter your lastname:")
    lastname = input()
    print("enter your Student ID number:")
    student_id = input()
    print("Your system login name is :")
    login.process_login(firstname,lastname,student_id)

main()


