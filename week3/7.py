num=int(input("Enter the number: "))
if 0<= num <=12:
    for i in range(13):
       print(f"{i} x {num} = {i*num}")
else:
    print("Please enter the number between 0 and 12")