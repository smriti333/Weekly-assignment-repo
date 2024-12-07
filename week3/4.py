BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password1=input("enter the new password1: ")
if 8 <= len(password1) <=12:
    if password1.lower() in BAD_PASSWORDS:
        print("Try another stronger password ")
    else:   
        password2=input("Re-enter the password2: ")
        if password1==password2:
          print("Password Set")
        else:
          print("Error")
else:
    print("the password must be between 8-12 characters long")
