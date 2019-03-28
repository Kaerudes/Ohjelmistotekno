

def main():
    string = input("Enter a String:")
    print("This is what i found out about the string")

    if string.isalnum() == True:
        print("The string is alphanumeric.")
    else:
        print("The String is not alphanumeric")


    if string.isalpha() == True:
        print("The string contains only alphabetic characters.")
    else:
         print("The String doesn't contain only alphabetic chars")

    if string.islower() == True:
        print("The letters in the string are all lowercase")
    else:
        print("The Letters are not all lowercase")

    if string.isupper() == True:
        print("Everything is uppercase")
    else:
        print("Everything is uppercase")

    if string.isdigit() == True:
        print("All is digit")
    else:
        ("All is digit")



main()