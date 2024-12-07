#num=int(input("Enter the number: ")) add this part as a test fucntion
#validating function whether it is in range or not:
def validate_input(num): #function calling using def
    if 0<= num <=100:
       return True
    else:
       return False

# test fucntion
test_num=int(input("Enter the number: "))

if validate_input(test_num):
    print(f'the {test_num} is in range 0 to 100')
else:
    print(f'the {test_num} is not in range 0 to 100')

