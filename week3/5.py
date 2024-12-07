BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True: #infinite loop 
   password1=input("enter the new password1: ")
   if not (8 <= len(password1) <=12):
       print("the password must be between 8-12 characters long")
       continue #Restrart the loop
   if password1.lower() in BAD_PASSWORDS:
        print("Try another stronger password ")
        continue
         
   password2=input("Re-enter the password2: ")
   if password1!=password2:
        print("Password do not match. Please try again")
        continue
   print("Password Set")
   break
    