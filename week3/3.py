password1=(input("Enter the new password1 8-12 characters: "))
if 8 <= len(password1) <=12:
    password2=input("Re-enter the password2: ")
    if password1==password2:
        print("Password Set")
    else:
        print("Error")
else:
     print("It must be between 8 and 12 characters long")
        